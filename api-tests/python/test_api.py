import pytest
import requests

from config.config import (
    API_BASE_URL
)

from utils.data_loader import (
    load_test_data
)


TEST_DATA = load_test_data()

API_DATA = TEST_DATA["api"]


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_posts():

    response = requests.get(
        f"{API_BASE_URL}/posts"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    assert "userId" in data[0]


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
def test_get_single_post():

    post_id = (
        API_DATA["valid_post_id"]
    )

    response = requests.get(
        f"{API_BASE_URL}/posts/{post_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id
    assert "title" in data
    assert data["body"] != ""


@pytest.mark.api
@pytest.mark.regression
def test_create_post():

    payload = API_DATA["post"]

    response = requests.post(
        f"{API_BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert "id" in data

    assert (
        data["title"]
        == payload["title"]
    )

    assert (
        data["userId"]
        == payload["userId"]
    )


@pytest.mark.api
@pytest.mark.regression
def test_update_post():

    payload = (
        API_DATA["updated_post"]
    )

    post_id = payload["id"]

    response = requests.put(
        f"{API_BASE_URL}/posts/{post_id}",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id

    assert (
        data["title"]
        == payload["title"]
    )

    assert (
        data["userId"]
        == payload["userId"]
    )


@pytest.mark.api
@pytest.mark.regression
def test_delete_post():

    post_id = (
        API_DATA["valid_post_id"]
    )

    response = requests.delete(
        f"{API_BASE_URL}/posts/{post_id}"
    )

    assert response.status_code == 200


@pytest.mark.api
@pytest.mark.regression
def test_invalid_post():

    post_id = (
        API_DATA["invalid_post_id"]
    )

    response = requests.get(
        f"{API_BASE_URL}/posts/{post_id}"
    )

    assert response.status_code == 404
