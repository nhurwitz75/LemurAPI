import json
from fastapi import FastAPI

app = FastAPI()

with open("data/lemurs.json") as f:
    lemurs = json.load(f)

@app.get("/lemurs")
def get_lemurs():
    return lemurs

@app.get("/lemurs/{id}")
def get_lemur(id: int):
    for lemur in lemurs:
        if lemur["id"] == id:
            return lemur
    return {"error": "Lemur not found"}, 404

@app.get("/lemurs")
def get_lemurs(mood: str = None):
    if mood:
        return [lemur for lemur in lemurs if lemur["palette"]["mood"].lower() == mood.lower()]
    return lemurs