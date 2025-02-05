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

    @allure.step('Регистрация нового пользователя c уже существующими данными')
    def create_user_with_existing_data(self):
        data = Data()
        payload = data.data_for_existing_user
        response = requests.post(f'{BASE_URL}{USERS_URL}/register', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Регистрация нового пользователя без ввода пароля')
    def create_new_user_without_password(self):
        generator = Generator()

        payload = {
            'email': generator.generate_random_email(5),
            'name': generator.generate_random_string(7)
        }

        response = requests.post(f'{BASE_URL}{USERS_URL}/register', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Авторизация под существующим пользователем')
    def user_login(self):
        generator = Generator()
        _, auth_data, _ = generator.create_random_user()

        payload = {
            'email': auth_data[0],
            'password': auth_data[1],
            'name': auth_data[2]
        }

        response = requests.post(f'{BASE_URL}{USERS_URL}/login', json=payload)
        token = response.json()['accessToken']
        return response.status_code, token

    @allure.step('Авторизация с неверным вводом email')
    def user_login_with_wrong_email(self):
        generator = Generator()
        data = Data
        status_code, password, name = generator.create_random_user()

        payload = {
            'email': data.wrong_email,
            'password': password,
            'name': name
        }

        response = requests.post(f'{BASE_URL}{USERS_URL}/login', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Авторизация с неверным вводом пароля')
    def user_login_with_wrong_password(self):
        generator = Generator()
        data = Data()
        status_code, email, name = generator.create_random_user()

        payload = {
            'email': email,
            'password': data.wrong_password,
            'name': name
        }

        response = requests.post(f'{BASE_URL}{USERS_URL}/login', json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Изменение данных под авторизованным пользователем')
    def change_user_data_authorized(self):
        generator = Generator()
        token = self.user_login()
        headers = {'Authorization': token[1]}

        payload = {
            'password': generator.generate_random_string(7)
        }

        response = requests.patch(f'{BASE_URL}{USERS_URL}/user', headers=headers, json=payload)
        return response.status_code, response.json()['user']

    @allure.step('Изменение данных пользователя без авторизации')
    def change_user_data_unauthorized(self):
        generator = Generator()

        payload = {
            'password': generator.generate_random_string(7)
        }

        response = requests.patch(f'{BASE_URL}{USERS_URL}/user', json=payload)
        return response.status_code, response.json()['message']
