import allure
import pytest
import requests
from api.endpoints import Endpoints
from data.test_data import UserMessages, Ingredients


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.description("Проверка успешного создания заказа авторизованным пользователем с валидными ингредиентами")
    def test_create_order_with_auth_and_ingredients_success(self, auth_header, valid_ingredients):
        response = requests.post(Endpoints.ORDERS, headers=auth_header, json=valid_ingredients)
        assert (response.status_code == 200 and
                response.json()["success"] is True and
                "order" in response.json())

    @allure.title("Создание заказа без авторизации, но с ингредиентами")
    @allure.description("Проверка создания заказа неавторизованным пользователем")
    def test_create_order_without_auth_with_ingredients_success(self, valid_ingredients):
        response = requests.post(Endpoints.ORDERS, json=valid_ingredients)
        assert (response.status_code == 200 and
                response.json()["success"] is True)

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка ошибки при попытке создать заказ без ингредиентов")
    def test_create_order_no_ingredients_failed(self, auth_header):
        response = requests.post(Endpoints.ORDERS, headers=auth_header, json={"ingredients": []})
        assert (response.status_code == 400 and
                response.json()["message"] == UserMessages.INGREDIENTS_REQUIRED)

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Проверка ошибки сервера при передаче невалидного хеша ингредиента")
    def test_create_order_invalid_ingredient_hash_failed(self, auth_header, invalid_ingredients):
        response = requests.post(Endpoints.ORDERS, headers=auth_header, json=invalid_ingredients)
        assert response.status_code == 500