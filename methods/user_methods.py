import requests
import allure
from data import Data
from urls import BASE_URL, USERS_URL
from helpers import Generator


class UserMethods:

    @allure.step('Регистрация нового пользователя')
    def create_new_user(self):
        generator = Generator()
        return generator.create_random_user()


    def try_to_create_user_with_existing_data(self):
        data = Data()
        payload = data.data_for_registration_same_user
        response = requests.post(f"{BASE_URL}{USERS_URL}/register", json=payload)
        return response.status_code, response.json()['message']

    def try_to_create_new_user_without_password(self):
        generator = Generator()

        payload = {
            "email": generator.generate_random_email(5),
            "name": generator.generate_random_string(7)
        }

        response = requests.post(f"{BASE_URL}{USERS_URL}/register", json=payload)
        return response.status_code, response.json()['message']

    def user_login(self):
        generator = Generator()
        _, auth_data, _ = generator.create_random_user()

        payload = {
            "email": auth_data[0],
            "password": auth_data[1]
        }

        response = requests.post(f"{BASE_URL}{USERS_URL}/login", json=payload)
        token = response.json()['accessToken']
        return response.status_code, str(token)

    def user_login_with_wrong_email(self):
        generator = Generator()
        data = Data
        status_code, email, password = generator.create_random_user()

        payload = {
            "email": data.wrong_email,
            "password": password
        }

        response = requests.post(f"{BASE_URL}{USERS_URL}/login", json=payload)
        return response.status_code, response.json()['message']

    def user_login_with_wrong_password(self):
        generator = Generator()
        data = Data()
        status_code, email, password = generator.create_random_user()

        payload = {
            'email': email,
            'password': data.wrong_password
        }

        response = requests.post(f"{BASE_URL}{USERS_URL}/login", json=payload)
        return response.status_code, response.json()['message']

    def change_user_data_authorized(self):
        generator = Generator()
        token = self.user_login()
        headers = {'Authorization': token[1]}

        payload = {
            'password': generator.generate_random_string(7)
        }

        response = requests.patch(f"{BASE_URL}{USERS_URL}/user", headers=headers, json=payload)
        return response.status_code, response.json()['user']

    def change_user_data_unauthorized(self):
        generator = Generator()

        payload = {
            'password': generator.generate_random_string(7)
        }

        response = requests.patch(f"{BASE_URL}{USERS_URL}/user", json=payload)
        return response.status_code, response.json()['message']


user_methods = UserMethods()
print(user_methods.user_login())