import os

from bson import ObjectId
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio

from models import UserModel, RecipeModel, ShoppingListItemModel
from utils import create_recipe

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


@app.post("/recipe/{id}", response_model=RecipeModel)
async def get_recipe(id: str):
    if (recipe := await db["recipes"].find_one({"_id": id})) is not None:
        return recipe

    raise HTTPException(status_code=404, detail="Recipe not found")


@app.post("/recipe")
async def create_recipe_helper(body: dict = Body(...)):
    # Search for exisitng username
    if (_ := await db["recipes"].find_one({"url": body["url"]})) is not None:
        raise HTTPException(status_code=404, detail="Recipe already exists")

    await create_recipe(db, body["url"])
    return


@app.put("/shopping_list/{item_id}/{is_bought}")
async def shopping_list_item_toggle_bought(item_id: str, is_bought: str):
    is_bought_bool = False
    if is_bought == "true":
        is_bought_bool = True
    elif is_bought != "false":
        raise HTTPException(status_code=404, detail="is_bought must be true or false")

    if (item := await db["shopping"].find_one({"_id": ObjectId(item_id)})) is not None:
        await db["shopping"].update_one(item, {"$set": {"is_bought": is_bought_bool}})
        return

    raise HTTPException(status_code=404, detail="Shopping list item not found")


@app.get("/shopping_list/", response_model=list[ShoppingListItemModel])
async def get_ingredients():
    ingredients = await db["shopping"].find().to_list(1000)
    return ingredients
