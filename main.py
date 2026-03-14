import json
from fastapi import FastAPI

app = FastAPI()

with open("data/lemurs.json") as f:
    lemurs = json.load(f)

@app.get("/lemurs")
def get_lemurs():
    return lemurs