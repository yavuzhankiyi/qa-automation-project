import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    assert "userId" in data[0]


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert data["body"] != ""


def test_create_post():
    payload = {
        "title": "QA Automation Project",
        "body": "API testing with Python",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["title"] == "QA Automation Project"
    assert data["userId"] == 1


def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated QA Project",
        "body": "Updated using Python",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated QA Project"
    assert data["userId"] == 1


def test_delete_post():
    response = requests.delete(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200


def test_invalid_post():
    response = requests.get(
        f"{BASE_URL}/posts/999999"
    )

    assert response.status_code == 404