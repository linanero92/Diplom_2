import requests
import allure
from data import Data
from urls import BASE_URL, ORDERS_URL
from methods.user_methods import UserMethods


class OrderMethods:

    @allure.step('Создание заказа под авторизованным пользователем')
    def make_order_authorized(self, email, password):
        data = Data
        user_methods = UserMethods()
        token = user_methods.user_login(email, password)
        headers = {'Authorization': str(token[1])}

        payload = {
            'ingredients': data.ingredients
        }

        response = requests.post(f'{BASE_URL}{ORDERS_URL}', headers=headers, json=payload)
        return response.status_code, response.json()

    @allure.step('Создание заказа без авторизации пользователя')
    def make_order_unauthorized(self):
        data = Data

        payload = {
            'ingredients': data.ingredients
        }

        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Создание заказа без добавления ингредиентов под авторизованным пользователем')
    def make_order_without_ingredients_authorized(self, email, password):
        data = Data
        user_methods = UserMethods()
        token = user_methods.user_login(email, password)
        headers = {'Authorization': str(token[1])}

        payload = {
            'ingredients': data.no_ingredients
        }

        response = requests.post(f'{BASE_URL}{ORDERS_URL}', headers=headers, json=payload)
        return response.status_code, response.json()['message']

    @allure.step('Создание заказа с невалидными ингредиентами без авторизации пользователя')
    def make_order_with_wrong_ingredients_unauthorized(self):
        data = Data

        payload = {
            'ingredients': data.one_wrong_ingredient
        }

        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code

    @allure.step('Получение списка заказов под авторизованным пользователем')
    def get_orders_list_authorized(self, headers):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers=headers)
        return response.status_code, response.json()

    @allure.step('Получение списка заказов без авторизации пользователя')
    def get_orders_list_unauthorized(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()['message']
