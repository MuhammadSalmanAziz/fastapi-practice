from fastapi import FastAPI,Depends,Query
from typing import Optional, List

app = FastAPI()

#Depedency Injection Class
class CommonParam:
    def __init__(self,q:Optional[int]=9, skip:int=10, limit:int=0):
        self.q= q
        self.skip = skip
        self.limit = limit

@app.get("/items")
async def read(commons:CommonParam = Depends(CommonParam)):
    return commons.q + commons.skip + commons.limit

#Dependecy Injection Functions

# async def common_param(q:Optional[str]=None, skip:int= 0, limit:int = 10):
#     return {"q": q, "skip":skip, "limit": limit}

# @app.get("/items")
# async def read_items(commons:dict= Depends(common_param)):
#     return commons