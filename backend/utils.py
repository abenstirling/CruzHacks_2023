from fastapi.encoders import jsonable_encoder
from recipe_scrapers import scrape_me
import json

from extract_test import parse_menu


async def create_recipe(db, url: str):
    scraper = scrape_me(url, wild_mode=True)

    # Create ingredient list
    res: str = await parse_menu(url)
    start = res.find("```") + 3
    end = res.rfind("```") - 1
    res = res[start:end]
    print(f"intermediate res is `{res}`")
    ingredients = json.loads(res)["ingredients"]

    cook_time = None
    try:
        cook_time = scraper.cook_time()
    except:
        cook_time = None

    recipe = {
        "title": scraper.title(),
        "url": url,
        "image": scraper.image(),
        "ingredients": ingredients,
        "instructions": scraper.instructions(),
        "cook_time": cook_time,
        "author": scraper.author(),
        "yields": scraper.yields(),
        "nutrition": parse_nutrition(scraper.nutrients())
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


def parse_nutrition(nutrition: dict):
    pretty_nutrition = {}

    for key in nutrition:
        amount = ""
        nutrition_unit = 0
        end_index = 0

        for i in range(len(nutrition[key])):
            if nutrition[key][i].isdigit():
                amount += nutrition[key][i]
            else:
                end_index = i
                break

        for i in range(end_index, len(nutrition[key])):
            if nutrition[key][i] == 'g':
                nutrition_unit = 1
                break
            elif nutrition[key][i] == 'm':
                nutrition_unit = 2
                break

        if nutrition_unit != 0 and amount != "":
            if key == "calories":
                pretty_nutrition[key] = int(amount)
            else:
                pretty_nutrition[key] = {
                    "amount": int(amount),
                    "unit": nutrition_unit
                }

    return pretty_nutrition
