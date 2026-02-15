import allure
import pytest
import requests
from api.endpoints import Endpoints
from data.test_data import UserMessages


class TestUpdateUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    @allure.description("Проверка успешного обновления полей пользователя при наличии авторизации")
    @pytest.mark.parametrize("update_data", [
        {"email": "new_email_auth@yandex.ru"},
        {"name": "NewAuthName"},
        {"email": "combined_auth@yandex.ru", "name": "CombinedAuthName"}
    ])
    def test_update_user_with_auth_success(self, registered_user, auth_header, update_data):
        response = requests.patch(Endpoints.USER, headers=auth_header, json=update_data)
        assert (response.status_code == 200 and
                response.json()["success"] is True)

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.description("Проверка ошибки при попытке обновления данных без токена авторизации")
    @pytest.mark.parametrize("update_data", [
        {"email": "new_email_noauth@yandex.ru"},
        {"name": "NewNoAuthName"},
        {"email": "combined_noauth@yandex.ru", "name": "CombinedNoAuthName"}
    ])
    def test_update_user_without_auth_failed(self, update_data):
        response = requests.patch(Endpoints.USER, json=update_data)
        assert (response.status_code == 401 and
                response.json()["message"] == UserMessages.UNAUTHORIZED)