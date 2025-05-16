import allure

from src.config import Config
from src.data import Data
from src.helpers import register_new_user_and_return_email_password_name


class TestLoginUser:

    @allure.title("Test authorization")
    def test_user_authorization(self, auth_api):
        email, password = Config.email, Config.password
        response = auth_api.login_user(email, password)
        assert response.json()['success'] == True

    @allure.title("Test required fields")
    def test_complete_data_user_authorization(self, auth_api):
        email, password = Config.email, Config.password
        response = auth_api.login_user('', password)
        result = response.json()['message']
        assert result == Data.DATALOGIN401
        assert response.status_code == 401

    @allure.title("Test incorrect login")
    def test_incorrect_login_and_password(self, auth_api):
        email, password, name = register_new_user_and_return_email_password_name()
        response = auth_api.login_user(email, password)
        result = response.json()["message"]
        assert result == Data.DATALOGIN401
        assert response.status_code == 401

