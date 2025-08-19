# Practing Fast API

from fastapi import FastAPI,Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    password:str
    address: Optional[str]= None

@app.get("/")
def index():
    return "Hello World"

# Practicing path parameters
# how it looks like
# https://salman.com/items/item_id(1,2,3 etc)

# @app.get("/items/{item_id}")
# def index_2(item_id:int):
#     return {"product_id": item_id}

# # Query Parameters

# @app.get("/items/")
# def que(q:int=0, m : Optional[int]= 10):
#     return {"product": q ," m": m}

# #filepath

# @app.get("/items/{filepath:path}")
# def ind(filepath:str):
#     return {"filepath": filepath}


@app.get("/items")
def index(q: Optional[str]=Query(None,max_length=5,min_length=2)):
    return {"q":q}

@app.post("/items/{user_id}")
def index(user_id:int,user:User):
    print(user_id)
    return user
    return "hello world"