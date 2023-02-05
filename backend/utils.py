from fastapi.encoders import jsonable_encoder
from recipe_scrapers import scrape_me
import json

from extract_test import parse_menu


async def create_recipe(db, url: str):
    scraper = scrape_me(url)

    # Create ingredient list
    res: str = await parse_menu(url)
    start = res.find("```") + 3
    end = res.rfind("```") - 1
    res = res[start:end]
    print(f"intermediate res is `{res}`")
    ingredients = json.loads(res)["ingredients"]

    recipe = {
        "title": scraper.title(),
        "url": url,
        "image": scraper.image(),
        "ingredients": ingredients,
        "instructions": scraper.instructions(),
        "cook_time": scraper.cook_time(),
        "author": scraper.author(),
        "yields": scraper.yields()
    }

    new_recipe = await db["recipes"].insert_one(recipe)
    created_recipe = await db["recipes"].find_one({"_id": new_recipe.inserted_id})
    await update_shopping_list(db, created_recipe)

    return created_recipe


async def update_shopping_list(db, recipe):
    shopping_list_item = None

    for ingredient in recipe["ingredients"]:
        if (item := await db["shopping"].find_one({"ingredient.name": ingredient["name"]})) is not None:
            # Assume quantities are all the same for now
            new_quantity = ingredient["quantity"] + item["ingredient"]["quantity"]
            shopping_list_item = await db["shopping"].update_one(item,
                                                                 {"$set": {"ingredient.quantity": new_quantity,
                                                                           "is_bought": False}})
        else:
            shopping_list_item = await db["shopping"].insert_one({"ingredient": jsonable_encoder(ingredient),
                                                                  "is_bought": False})
    return shopping_list_item
