# Practing Fast API

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello World"

@app.get("/1")
def index1():
    return {"name": "salman"}