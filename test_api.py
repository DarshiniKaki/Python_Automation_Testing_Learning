import requests


def test_post_api():
    data = {
        "title": "test",
        "body": "automation",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 201
    assert response.json()["title"] == "test"