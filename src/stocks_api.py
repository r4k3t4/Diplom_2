import requests
from allure import step
from src.config import URL


class AuthAPI:

    def __init__(self, url: str):
        self.url = url

    @step("Create user")
    def create_user(self, email, password, name):
        data = {"email": email, "password": password, "name": name}
        response = requests.post(f"{self.url}{URL.CREATING_USER}", json=data)
        return response

    @step("Login user")
    def login_user(self, email, password):
        data = {"email": email, "password": password}
        response = requests.post(f"{self.url}{URL.USER_LOGIN}", json=data)
        return response

    @step("Change user data")
    def change_user_data(self, token, data):
        response = requests.patch(f"{self.url}{URL.CHANGING_USER_DATA}", headers=token, data=data)
        return response

    @step("Create order")
    def create_order(self, token, ingredients):
        data = {"ingredients": ingredients}
        response = requests.post(f"{self.url}{URL.CREATE_ORDER}", headers=token, data=data)
        return response

    @step("Get list ingredients")
    def get_ingredients(self):
        response = requests.get(f"{self.url}{URL.LIST_INGREDIENTS}")
        return response

    @step("List of orders")
    def receiving_list_orders(self, token):
        response = requests.get(f"{self.url}{URL.LIST_ORDER}", headers=token)
        return response
