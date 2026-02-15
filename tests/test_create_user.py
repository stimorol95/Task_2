import allure
import pytest
import requests
from api.endpoints import Endpoints
from data.test_data import UserMessages, UserData


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка успешного создания нового пользователя с уникальными данными")
    def test_create_unique_user_success(self, registered_user):
        response = registered_user["response"]
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Проверка ошибки при попытке создать уже существующего пользователя")
    def test_create_existing_user_failed(self, existing_user):
        payload = existing_user["payload"]
        response = requests.post(Endpoints.REGISTER, json=payload)
        assert (response.status_code == 403 and
                response.json()["message"] == UserMessages.USER_EXISTS)

    @pytest.mark.parametrize("incomplete_payload", UserData.MISSING_FIELDS)
    @allure.title("Создание пользователя без обязательного поля: {incomplete_payload}")
    @allure.description("Проверка ошибки при отсутствии одного из обязательных полей")
    def test_create_user_missing_field_failed(self, incomplete_payload):
        response = requests.post(Endpoints.REGISTER, json=incomplete_payload)
        assert (response.status_code == 403 and
                response.json()["message"] == UserMessages.REQUIRED_FIELDS)