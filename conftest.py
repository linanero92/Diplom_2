import pytest
import requests
from helpers import Generator
from urls import *
from methods.user_methods import UserMethods


@pytest.fixture()
def create_user_and_delete():
    email = Generator.generate_random_email(5)
    password = Generator.generate_random_string(7)
    name = Generator.generate_random_string(7)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f"{BASE_URL}{AUTH_URL}{REGISTER_URL}", json=payload)
    response_json = response.json()
    token = response_json.get('accessToken')
    yield email, password, name, token
    headers = {'Authorization': str(token[1])}
    requests.delete(f'{BASE_URL}{AUTH_URL}{USER_URL}', headers=headers)


@pytest.fixture()
def delete_user_from_test_user_create():
    user_methods = UserMethods()
    response = user_methods.create_user()
    response_json = response.json()
    token = response_json.get('accessToken')
    yield token
    headers = {'Authorization': str(token[1])}
    requests.delete(f'{BASE_URL}{AUTH_URL}{USER_URL}', headers=headers)