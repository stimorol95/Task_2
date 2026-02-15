import allure
import requests
from api.endpoints import Endpoints
from data.test_data import UserMessages, UserData
from helpers.user_helper import login_user


class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    @allure.description("Проверка успешной авторизации зарегистрированного пользователя")
    def test_login_existing_user_success(self, existing_user):
        credentials = {
            "email": existing_user["payload"]["email"],
            "password": existing_user["payload"]["password"]
        }
        response = login_user(credentials)
        assert (response.status_code == 200 and
                response.json()["success"] is True and
                "accessToken" in response.json())

    @allure.title("Логин с неверным логином и паролем")
    @allure.description("Проверка ошибки авторизации с некорректными учетными данными")
    def test_login_invalid_credentials_failed(self):
        response = login_user(UserData.INVALID_CREDENTIALS)
        assert (response.status_code == 401 and
                response.json()["message"] == UserMessages.INCORRECT_LOGIN)