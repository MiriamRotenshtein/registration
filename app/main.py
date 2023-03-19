from typing import List
from typing import Union
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str 
    
  
users = [User(id=000000000, name="esty")]

@app.get("/users/")
async def get_users():
    with open("data.json","r") as f:
        try:
            users=json.load(f)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Unable to read payloads from file")
    last_payloads = users[-10:]
    return last_payloads

@app.post("/users")
async def add_user(user:User):
    users.append(user)
    with open("data.json","w") as f:
        json.dump([dict(user) for user in users], f)
    return {"message": "Payload added successfully"}
