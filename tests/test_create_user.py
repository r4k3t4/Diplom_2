import pytest
from src.helpers import register_new_user_and_return_email_password_name
from src.data import Data
import allure
from src.config import Config


class TestCreateUser:

    @allure.title("Test for create user")
    def test_user_create(self, new_user):
        response = new_user
        assert response.json()['success'] == True

    @allure.title("Test for creating identical users")
    def test_users_duplication(self, auth_api):
        email, password, name = register_new_user_and_return_email_password_name()
        response = auth_api.create_user(email, password, name)
        response = auth_api.create_user(email, password, name)
        assert response.json()['message'] == Data.REG403
        assert response.status_code == 403

    @allure.title("Test required fields")
    def test_complete_data_user_create(self, auth_api):
        email, password, name = register_new_user_and_return_email_password_name()
        response = auth_api.create_user('', password, name)
        assert response.json()['message'] == Data.DATAREG400
        assert response.status_code == 403
