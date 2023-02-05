from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_item():
    response = client.post(
        "/",
        headers={"X-Token": "coneofsilence"},
        json={
          "name": "Jane Doe",
          "email": "jdoe@example.com",
          "course": "Experiments, Science, and Fashion in Nanophotonics",
          "gpa": "3.0"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Jane Doe",
        "email": "jdoe@example.com",
        "course": "Experiments, Science, and Fashion in Nanophotonics",
        "gpa": "3.0"
    }
