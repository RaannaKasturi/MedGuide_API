from fastapi import FastAPI, Request
from getData import get_list

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/query/{drug_query}")
def get_drug_list(drug_query: str):
    return get_list(drug_query)