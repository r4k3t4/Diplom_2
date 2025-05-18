from src.data import Data
from src.helpers import register_new_user_and_return_email_password_name
import allure


class TestChangingUserData:

    @allure.title("Test changing user email without token")
    def test_changing_user_email_without_auth(self, new_user, auth_api):
        r = new_user
        email = register_new_user_and_return_email_password_name()[0]
        newdata = {'email': email}
        token = {'authorization': ''}
        response = auth_api.change_user_data(token, newdata)
        assert response.json()['success'] == False and response.json()['message'] == Data.DATACHANGE401

    @allure.title("Test changing user email with token")
    def test_changing_user_email_with_auth(self, new_user, auth_api):
        r = new_user
        email = register_new_user_and_return_email_password_name()[0]
        newdata = {'email': email}
        token = {'authorization': r.json()['accessToken']}
        response = auth_api.change_user_data(token, newdata)
        assert response.status_code == 200 and response.json()["user"]["email"] == newdata["email"]

    @allure.title("Test changing user name without token")
    def test_changing_user_name_without_auth(self, new_user, auth_api):
        r = new_user
        name = register_new_user_and_return_email_password_name()[2]
        newdata = {'name': name}
        token = {'authorization': ''}
        response = auth_api.change_user_data(token, newdata)
        assert response.json()['success'] == False and response.json()['message'] == Data.DATACHANGE401

    @allure.title("Test changing user name with token")
    def test_changing_user_name_with_auth(self, new_user, auth_api):
        r = new_user
        name = register_new_user_and_return_email_password_name()[2]
        newdata = {'name': name}
        token = {'authorization': r.json()['accessToken']}
        response = auth_api.change_user_data(token, newdata)
        assert response.status_code == 200 and response.json()["user"]["name"] == newdata["name"]

