import json
from fastapi import FastAPI

app = FastAPI()

with open("data/lemurs.json") as f:
    lemurs = json.load(f)

@app.get("/lemurs")
def get_lemurs(mood: str = None, conservation_status = None):
    result = lemurs
    if mood:
        return [lemur for lemur in lemurs if lemur["palette"]["mood"].lower() == mood.lower()]
    if conservation_status:
        return [lemur for lemur in lemurs if lemur["conservation_status"].lower() == status.lower()]
    return lemurs 

@app.get("/lemurs/{id}")
def get_lemur(id: int):
    for lemur in lemurs:
        if lemur["id"] == id:
            return lemur
    return {"error": "Lemur not found"}, 404