import allure
import pytest
from data.test_data import UserMessages, UserData
from helpers.user_helper import update_user


class TestUpdateUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    @allure.description("Проверка успешного обновления полей пользователя при наличии авторизации")
    def test_update_user_with_auth_success(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Подготовка уникальных данных для обновления
        update_data = {
            "email": UserData.generate_unique_email(),
            "name": UserData.generate_unique_name()
        }
        # Шаг 3: Обновление данных пользователя
        response = update_user(access_token, update_data)
        response_body = response.json()
        # Шаг 4: Проверка успешного обновления
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                response_body["user"]["email"] == update_data["email"] and
                response_body["user"]["name"] == update_data["name"])

    @allure.title("Изменение только email пользователя с авторизацией")
    @allure.description("Проверка успешного обновления email пользователя")
    def test_update_user_email_with_auth_success(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Подготовка уникального email для обновления
        update_data = {"email": UserData.generate_unique_email()}
        # Шаг 3: Обновление email пользователя
        response = update_user(access_token, update_data)
        response_body = response.json()
        # Шаг 4: Проверка успешного обновления
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                response_body["user"]["email"] == update_data["email"])

    @allure.title("Изменение только имени пользователя с авторизацией")
    @allure.description("Проверка успешного обновления имени пользователя")
    def test_update_user_name_with_auth_success(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Подготовка уникального имени для обновления
        update_data = {"name": UserData.generate_unique_name()}
        # Шаг 3: Обновление имени пользователя
        response = update_user(access_token, update_data)
        response_body = response.json()
        # Шаг 4: Проверка успешного обновления
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                response_body["user"]["name"] == update_data["name"])

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.description("Проверка ошибки при попытке обновления данных без токена авторизации")
    def test_update_user_without_auth_failed(self):
        # Шаг 1: Подготовка данных для обновления
        update_data = {"name": "NewNameWithoutAuth"}
        # Шаг 2: Попытка обновления данных без авторизации
        response = update_user(None, update_data)
        response_body = response.json()
        # Шаг 3: Проверка ошибки
        assert (response.status_code == 401 and 
                response_body["success"] is False and 
                response_body["message"] == UserMessages.UNAUTHORIZED)