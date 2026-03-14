import json
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

with open("data/lemurs.json") as f:
    lemurs = json.load(f)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/lemurs")
def get_lemurs(mood: str = None, conservation_status = None, common_name = None):
    result = lemurs
    if mood:
        result = [lemur for lemur in result if lemur["palette"]["mood"].lower() == mood.lower()]
    if conservation_status:
        result = [lemur for lemur in result if lemur["conservation_status"].lower() == conservation_status.lower()]
    if common_name:
        result = [lemur for lemur in result if common_name.lower() in lemur["common_name"].lower()] 
    return result

@app.get("/lemurs/{id}")
def get_lemur(id: int):
    for lemur in lemurs:
        if lemur["id"] == id:
            return lemur
    return {"error": "Lemur not found"}, 404