import pytest
from httpx import AsyncClient

from main import app, db
from utils import update_shopping_list

TEST_INGREDIENTS = [
    {
       "name": "egg",
       "quantity": 2.0,
       "unit": "none",
       "qualifiers": ["large"]
    },
    {
       "name": "sea salt",
       "quantity": 1.0,
       "unit": "pinch",
       "qualifiers": ["fine"]
    },
    {
       "name": "butter",
       "quantity": 0.5,
       "unit": "tbsp",
       "qualifiers": ["unsalted"]
    },
    {
       "name": "sweet potatoes",
       "quantity": 3.0,
       "unit": "none",
       "qualifiers": []
    },
    {
       "name": "mozzarella",
       "quantity": 0.25,
       "unit": "cup",
       "qualifiers": ["shredded", "low moisture", "part-skim"]
    },
    {
       "name": "chives",
       "quantity": 6.0,
       "unit": "none",
       "qualifiers": []
    }
]


TEST_RECIPE = {
    "title": "Banana muffins",
    "url": "https://www.allrecipes.com/recipe/257206/ultimate-banana-muffins/",
    "image": "placeholder",
    "ingredients": TEST_INGREDIENTS,
    "cook_time": 60,
    "author": "placeholder",
    "yields": "placeholder"
}

TEST_RECIPE_2 = {
    "title": "Not Banana muffins",
    "url": "https://www.allrecipes.com/recipe/257206/ultimate-banana-muffins/",
    "image": "placeholder",
    "ingredients": [
        {
            "name": "egg",
            "quantity": 2.0,
            "unit": "none",
            "qualifiers": ["large"]
        },
        {
            "name": "butter",
            "quantity": 0.5,
            "unit": "tbsp",
            "qualifiers": ["unsalted"]
        },
    ],
    "cook_time": 60,
    "author": "placeholder",
    "yields": "placeholder"
}


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        print("Client is ready")
        yield client
#
#
# @pytest.mark.anyio
# async def test_create_user(client: AsyncClient):
#     response = await client.post(
#         "/user/create",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "userName": "Bob Bob",
#             "password": "securePassword123"
#         }
#     )
#
#     assert response.status_code == 201  # Create new database entry
#     assert response.json()["userName"] == "Bob Bob"
#     assert response.json()["password"] == "securePassword123"


@pytest.mark.anyio
async def test_create_user_duplicate_username(client: AsyncClient):
    response = await client.post(
        "/user/create",
        headers={"X-Token": "coneofsilence"},
        json={
            "userName": "Bob Bob",
            "password": "securePassword456"
        }
    )

    assert response.status_code == 404


@pytest.mark.anyio
async def test_login_user_success(client: AsyncClient):
    response = await client.post(
        "/user/login/",
        headers={"X-Token": "coneofsilence"},
        json={
            "userName": "Bob Bob",
            "password": "securePassword123"
        }
    )

    assert response.status_code == 200
    assert response.json()["userName"] == "Bob Bob"
    assert response.json()["password"] == "securePassword123"


@pytest.mark.anyio
async def test_login_user_incorrect_password(client: AsyncClient):
    response = await client.post(
        "/user/login/",
        headers={"X-Token": "coneofsilence"},
        json={
            "userName": "Bob Bob",
            "password": "insecurePassword123"
        }
    )

    assert response.status_code == 404


@pytest.mark.anyio
async def test_login_user_incorrect_username(client: AsyncClient):
    response = await client.post(
        "/user/login/",
        headers={"X-Token": "coneofsilence"},
        json={
            "userName": "Boba Boba",
            "password": "securePassword123"
        }
    )

    assert response.status_code == 404


@pytest.mark.anyio
async def test_update_shopping_list(client: AsyncClient):
    await update_shopping_list(db, TEST_RECIPE_2)


@pytest.mark.anyio
async def test_shopping_list_item_toggle_bought(client: AsyncClient):
    response = await client.put(
        "/shopping_list/63df5b5f66be67c60c764905/false",
        headers={"X-Token": "coneofsilence"}
    )

    assert response.status_code == 200


@pytest.mark.anyio
async def test_create_recipe(client: AsyncClient):
    response = await client.post(
        "/recipe",
        headers={"X-Token": "coneofsilence"},
        json={
            "url": "https://www.allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/"
        }
    )

    assert response.status_code == 200


# @pytest.mark.anyio
# async def test_get_shopping_list(client: AsyncClient):
#     response = await client.get(
#         "/shopping_list/",
#         headers={"X-Token": "coneofsilence"},
#     )
#
#     assert response.status_code == 200
#     assert response.json() == TEST_INGREDIENTS
