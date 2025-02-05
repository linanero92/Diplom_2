import pytest
import requests
from helpers import Generator
from urls import *

@pytest.fixture
def create_new_user_and_delete():
    generator = Generator()
    auth_data, token = generator.create_random_user()
    yield token, auth_data
    headers = {'Authorization': token[1]}
    requests.delete(f'{BASE_URL}{USERS_URL}/user', headers=headers)