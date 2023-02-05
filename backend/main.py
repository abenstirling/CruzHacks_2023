import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
from models import UserModel

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.mealPlanner


@app.post("/user/create", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):
    user = jsonable_encoder(user)

    # Search for exisitng username
    if (db_user := await db["users"].find_one({"userName": user["userName"]})) is not None:
        raise HTTPException(status_code=404, detail="Username already exists")

    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@app.post("/user/login/", response_model=UserModel)
async def login_user(user: UserModel = Body(...)):
    if (db_user := await db["users"].find_one({"userName": user.userName, "password": user.password})) is not None:
        return db_user
    else:
        raise HTTPException(status_code=404, detail=f"User {user.userName} not found or password doesn't match")
