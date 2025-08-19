from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import session

from app.database import engine, sessionLocal, Base

#MOdel
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index= True)
    email = Column(String, index= True)
    is_active = Column(Boolean)

    class Config:
        orm_mode = True

#Schema
class UserSchema(BaseModel):
    id: int
    email: str
    is_active:bool

#For depedency Injection
def get_db():
    db = sessionLocal()
    try:
        yield db

    finally:
        db.close()


Base.metadata.create_all(bind = engine)

app = FastAPI()

@app.post("/users",response_model=UserSchema)
def write_data(user:UserSchema, db:session= Depends(get_db)):
    #db work
    u = User(id = user.id,email = user.email,is_active = user.is_active)
    db.add(u)
    db.commit()
    return u

@app.get("/users",response_model=List[UserSchema])
def get_data(db:session=Depends(get_db)):
    return db.query(User).all()