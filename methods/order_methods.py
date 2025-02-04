import requests
import allure
from data import Data
from urls import BASE_URL, ORDERS_URL
from helpers import Generator
from methods.user_methods import UserMethods

class OrderMethods:

    def make_order_authorized(self):
        data = Data
        user_methods = UserMethods
        token = user_methods.user_login()
        headers = {'Authorization': token[1]}

        payload = {
            "ingredients": data.ingredients
        }

        response = requests.post(f"{BASE_URL}{ORDERS_URL}", headers=headers, json=payload)
