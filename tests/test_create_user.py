import allure
import pytest
from data.test_data import UserMessages, UserData
from helpers.user_helper import register_user


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка успешного создания нового пользователя с уникальными данными")
    def test_create_unique_user_success(self):
        # Шаг 1: Подготовка данных уникального пользователя
        user_data = UserData.generate_unique_user()
        # Шаг 2: Регистрация пользователя
        response = register_user(user_data)
        response_body = response.json()
        # Шаг 3: Проверка успешного создания
        expected_user = {
            "email": user_data["email"],
            "name": user_data["name"]
        }
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                response_body["user"] == expected_user and
                "accessToken" in response_body and
                "refreshToken" in response_body)

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Проверка ошибки при попытке создать уже существующего пользователя")
    def test_create_existing_user_failed(self):
        # Шаг 1: Подготовка данных пользователя
        user_data = UserData.EXISTING_USER.copy()
        # Шаг 2: Первая регистрация (пользователь создается)
        response_first = register_user(user_data)
        # Шаг 3: Вторая попытка регистрации того же пользователя
        response_second = register_user(user_data)
        response_body = response_second.json()
        # Шаг 4: Проверка ошибки
        assert (response_second.status_code == 403 and 
                response_body["success"] is False and 
                response_body["message"] == UserMessages.USER_EXISTS)

    @pytest.mark.parametrize("incomplete_payload", UserData.MISSING_FIELDS)
    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Проверка ошибки при отсутствии одного из обязательных полей")
    def test_create_user_missing_field_failed(self, incomplete_payload):
        # Шаг 1: Попытка регистрации с неполными данными
        response = register_user(incomplete_payload)
        response_body = response.json()
        # Шаг 2: Проверка ошибки
        assert (response.status_code == 403 and 
                response_body["success"] is False and 
                response_body["message"] == UserMessages.REQUIRED_FIELDS)