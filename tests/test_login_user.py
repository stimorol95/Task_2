import allure
from data.test_data import UserMessages, UserData
from helpers.user_helper import login_user


class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    @allure.description("Проверка успешной авторизации зарегистрированного пользователя")
    def test_login_existing_user_success(self, existing_user_credentials):
        # Шаг 1: Попытка авторизации с корректными данными
        response = login_user(existing_user_credentials)
        response_body = response.json()
        # Шаг 2: Проверка успешной авторизации
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                response_body["user"]["email"] == existing_user_credentials["email"] and
                "accessToken" in response_body and
                "refreshToken" in response_body)

    @allure.title("Логин с неверным логином и паролем")
    @allure.description("Проверка ошибки авторизации с некорректными учетными данными")
    def test_login_invalid_credentials_failed(self):
        # Шаг 1: Попытка авторизации с некорректными данными
        response = login_user(UserData.INVALID_CREDENTIALS)
        response_body = response.json()
        # Шаг 2: Проверка ошибки
        assert (response.status_code == 401 and 
                response_body["success"] is False and 
                response_body["message"] == UserMessages.INCORRECT_LOGIN)