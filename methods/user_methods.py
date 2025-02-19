import requests
import allure
from data import Data
from urls import *
from helpers import Generator


class UserMethods:

    def create_user(self):
        email = Generator.generate_random_email(5)
        password = Generator.generate_random_string(7)
        name = Generator.generate_random_string(7)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(f"{BASE_URL}{AUTH_URL}{REGISTER_URL}", json=payload)
        print(response.json())
        response_json = response.json()
        token = response_json.get('accessToken')
        return token, response.status_code, response_json

    @allure.step('Регистрация нового пользователя c уже существующими данными')
    def create_user_with_existing_data(self):
        data = Data()
        payload = data.data_for_existing_user
        response = requests.post(f'{BASE_URL}{AUTH_URL}{REGISTER_URL}', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Регистрация нового пользователя без ввода пароля')
    def create_new_user_without_password(self, email, name):

        payload = {
            'email': email,
            'name': name
        }

        response = requests.post(f'{BASE_URL}{AUTH_URL}{REGISTER_URL}', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Авторизация под существующим пользователем')
    def user_login(self, email, password):

        payload = {
            'email': email,
            'password': password
        }

        response = requests.post(f'{BASE_URL}{AUTH_URL}{LOGIN_URL}', json=payload)
        token = response.json()['accessToken']
        return token, response.status_code, response.json()

    @allure.step('Авторизация с неверным вводом email')
    def user_login_with_wrong_email(self, password, name):
        data = Data

        payload = {
            'email': data.wrong_email,
            'password': password,
            'name': name
        }

        response = requests.post(f'{BASE_URL}{AUTH_URL}{LOGIN_URL}', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Авторизация с неверным вводом пароля')
    def user_login_with_wrong_password(self, email, name):
        data = Data()

        payload = {
            'email': email,
            'password': data.wrong_password,
            'name': name
        }

        response = requests.post(f'{BASE_URL}{AUTH_URL}{LOGIN_URL}', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Изменение данных под авторизованным пользователем')
    def change_user_data_authorized(self, email, password):
        token, _, _ = self.user_login(email, password)
        headers = {'Authorization': str(token)}
        generator = Generator()

        payload = {
            'email': generator.generate_random_email(5)
        }

        response = requests.patch(f'{BASE_URL}{AUTH_URL}{USER_URL}', headers=headers, json=payload)
        return response.status_code, response.json()

    @allure.step('Изменение данных пользователя без авторизации')
    def change_user_data_unauthorized(self):
        generator = Generator()

        payload = {
            'password': generator.generate_random_string(7)
        }

        response = requests.patch(f'{BASE_URL}{AUTH_URL}{USER_URL}', json=payload)
        return response.status_code, response.json()['message']
