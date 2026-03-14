import json
from fastapi import FastAPI

app = FastAPI()

with open("data/lemurs.json") as f:
    lemurs = json.load(f)

@app.get("/lemurs")
def get_lemurs(mood: str = None, conservation_status = None):
    result = lemurs
    if mood:
        result = [lemur for lemur in lemurs if lemur["palette"]["mood"].lower() == mood.lower()]
    if conservation_status:
        result = [lemur for lemur in lemurs if lemur["conservation_status"].lower() == conservation_status.lower()]
    return result

@app.get("/lemurs/{id}")
def get_lemur(id: int):
    for lemur in lemurs:
        if lemur["id"] == id:
            return lemur
    return {"error": "Lemur not found"}, 404