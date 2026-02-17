import allure
import pytest
from data.test_data import UserMessages, Ingredients
from helpers.user_helper import create_order


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.description("Проверка успешного создания заказа авторизованным пользователем")
    def test_create_order_with_auth_and_ingredients_success(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Создание заказа с валидными ингредиентами
        response = create_order(access_token, Ingredients.VALID_INGREDIENTS_REQUEST)
        response_body = response.json()
        # Шаг 3: Проверка успешного создания заказа
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                "name" in response_body and
                "order" in response_body and
                "number" in response_body["order"])

    @allure.title("Создание заказа без авторизации, но с ингредиентами")
    @allure.description("Проверка создания заказа неавторизованным пользователем")
    def test_create_order_without_auth_with_ingredients_success(self):
        # Шаг 1: Создание заказа без авторизации
        response = create_order(None, Ingredients.VALID_INGREDIENTS_REQUEST)
        response_body = response.json()
        # Шаг 2: Проверка успешного создания заказа
        assert (response.status_code == 200 and 
                response_body["success"] is True and 
                "name" in response_body and
                "order" in response_body and
                "number" in response_body["order"])

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка ошибки при попытке создать заказ без ингредиентов")
    def test_create_order_no_ingredients_failed(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Попытка создания заказа без ингредиентов
        response = create_order(access_token, Ingredients.EMPTY_INGREDIENTS_REQUEST)
        response_body = response.json()
        # Шаг 3: Проверка ошибки
        assert (response.status_code == 400 and 
                response_body["success"] is False and 
                response_body["message"] == UserMessages.INGREDIENTS_REQUIRED)

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Проверка ошибки сервера при передаче невалидного хеша")
    def test_create_order_invalid_ingredient_hash_failed(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Попытка создания заказа с невалидным хешем
        response = create_order(access_token, Ingredients.INVALID_INGREDIENTS_REQUEST)
        # Шаг 3: Проверка ошибки сервера (500 возвращает только статус, без тела)
        assert response.status_code == 500