import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
from models import UserModel

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.mealPlanner

@app.post("/user/create", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    new_user= await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)

@app.get("/user/login/", response_model=UserModel)
async def login_user(userName: str, password: str):
    if (user := await db["users"].find_one({"userName": userName})) is not None and (user["password"] == password):
        return user
    else:
        raise HTTPException(status_code=404, detail=f"User {userName} not found or password doesn't match")






