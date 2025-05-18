import allure

from src.data import Data


class TestListOrders:

    @allure.title("Receiving a list of orders without authorization")
    def test_list_orders_without_auth(self, auth_api):
        response = auth_api.receiving_list_orders(token='')
        assert response.status_code == 401 and response.json()["message"] == Data.ORDERLIST401 and response.json()['success'] == False

    @allure.title("Receiving a list of orders with authorization")
    def test_list_orders_without_auth(self, auth_api, new_user):
        token = {'authorization': new_user.json()['accessToken']}
        response = auth_api.receiving_list_orders(token)
        assert response.status_code == 200  and response.json()['success'] == True