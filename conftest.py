import pytest
from src.config import URL
from src.stocks_api import AuthAPI
from src.helpers import register_new_user_and_return_email_password_name


@pytest.fixture
def auth_api():
    return AuthAPI(URL.BASE_URL)


@pytest.fixture
def new_user(auth_api):
    email, password, name = register_new_user_and_return_email_password_name()
    response = auth_api.create_user(email, password, name)
    return response