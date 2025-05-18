import allure

from src.data import Data


class TestCreateOrder:
    @allure.title("Test create order without auth")
    def test_create_order_without_auth(self, auth_api):
        r = auth_api.get_ingredients()
        ingredients = r.json()["data"][0]["_id"]
        response = auth_api.create_order(token='', ingredients=ingredients)
        assert response.json()["success"] == True

    @allure.title("Test create order with auth")
    def test_create_order_with_auth(self, auth_api, new_user):
        token = {'authorization': new_user.json()['accessToken']}
        r = auth_api.get_ingredients()
        ingredients = r.json()["data"][0]["_id"]
        response = auth_api.create_order(token, ingredients)
        assert response.json()["success"] == True

    @allure.title("Test create order with ingredient")
    def test_create_order_with_ingredients(self, auth_api):
        r = auth_api.get_ingredients()
        ingredients = r.json()["data"][0]["_id"]
        response = auth_api.create_order(token='', ingredients=ingredients)
        assert response.json()["success"] == True

    @allure.title("Test create order without ingredient")
    def test_create_order_without_ingredients(self, auth_api):
        response = auth_api.create_order(token='', ingredients='')
        assert response.json()["success"] == False and response.status_code == 400 and response.json()[
            "message"] == Data.INGREDIENT400

    @allure.title("Test create order invalid hash ingredient")
    def test_create_order_invalid_hash_ingridient(self, auth_api):
        r = auth_api.get_ingredients()
        ingredients = r.json()["data"][0]["_id"] + '2'
        response = auth_api.create_order(token='', ingredients=ingredients)
        assert response.status_code == 500

