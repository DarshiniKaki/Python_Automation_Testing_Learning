import requests


def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200
    assert "username" in response.json()