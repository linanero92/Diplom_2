import random
import string
import requests
from urls import *
import allure

class Generator:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generate_random_email(length):
        characters = string.digits
        digits = ''.join(random.choice(characters) for _ in range(length))
        return f"test_user_{digits}@ya.ru"

    def create_random_user(self):
        email = Generator.generate_random_email(5)
        password = Generator.generate_random_string(7)
        name = Generator.generate_random_string(7)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        auth_data = [email, password, name]
        response = requests.post(f"{BASE_URL}{USERS_URL}/register", json=payload)
        response_json = response.json()
        token = response_json.get('accessToken')
        return response.status_code, auth_data, token


generator = Generator()
print(generator.create_random_user())