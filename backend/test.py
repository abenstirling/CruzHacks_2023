import pytest
from main import app
from httpx import AsyncClient


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
