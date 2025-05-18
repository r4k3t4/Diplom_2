class Config:
    email = 'neznaika@yandex.we'
    password = '123321'
    newpassword = '321123'


class URL:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    CREATING_USER = "/api/auth/register"
    USER_LOGIN = "/api/auth/login"
    CHANGING_USER_DATA = "/api/auth/user"
    CREATE_ORDER = "/api/orders"
    LIST_INGREDIENTS = "/api/ingredients"
    LIST_ORDER = "/api/orders"
