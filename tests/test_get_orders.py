import allure
from data.test_data import UserMessages
from helpers.user_helper import get_user_orders


class TestGetUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    @allure.description("Проверка успешного получения списка заказов для авторизованного пользователя")
    def test_get_orders_with_auth_success(self, created_user):
        # Шаг 1: Получение токена авторизации
        access_token = created_user["access_token"]
        # Шаг 2: Запрос списка заказов
        response = get_user_orders(access_token)
        response_body = response.json()
        # Шаг 3: Проверки
        assert response.status_code == 200
        assert response_body["success"] is True
        assert "orders" in response_body
        assert "total" in response_body
        assert "totalToday" in response_body

    @allure.title("Получение заказов неавторизованного пользователя")
    @allure.description("Проверка ошибки при попытке получить заказы без авторизации")
    def test_get_orders_without_auth_failed(self):
        # Шаг 1: Запрос списка заказов без авторизации
        response = get_user_orders(None)
        response_body = response.json()
        # Шаг 2: Проверки
        assert response.status_code == 401
        assert response_body["success"] is False
        assert response_body["message"] == UserMessages.UNAUTHORIZED