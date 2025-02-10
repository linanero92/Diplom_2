import pytest
import requests
from helpers import Generator
from urls import *


@pytest.fixture(scope='function')
def create_user_and_delete():
    email = Generator.generate_random_email(5)
    password = Generator.generate_random_string(7)
    name = Generator.generate_random_string(7)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f"{BASE_URL}{USERS_URL}/register", json=payload)
    response_json = response.json()
    token = response_json.get('accessToken')
    yield email, password, name, token, response.status_code
    headers = {'Authorization': token[1]}
    requests.delete(f'{BASE_URL}{USERS_URL}/user', headers=headers)
