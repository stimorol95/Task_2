import allure
import requests
from api.endpoints import Endpoints
from data.test_data import UserMessages


class TestGetUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    @allure.description("Проверка успешного получения списка заказов для авторизованного пользователя")
    def test_get_orders_with_auth_success(self, auth_header):
        response = requests.get(Endpoints.ORDERS, headers=auth_header)
        assert (response.status_code == 200 and
                response.json()["success"] is True and
                "orders" in response.json())

    @allure.title("Получение заказов неавторизованного пользователя")
    @allure.description("Проверка ошибки при попытке получить заказы без авторизации")
    def test_get_orders_without_auth_failed(self):
        response = requests.get(Endpoints.ORDERS)
        assert (response.status_code == 401 and
                response.json()["message"] == UserMessages.UNAUTHORIZED)