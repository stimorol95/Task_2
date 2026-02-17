import allure
import requests
from api.endpoints import Endpoints


@allure.step("Регистрация нового пользователя")
def register_user(payload):
    """Регистрация нового пользователя с переданными данными"""
    response = requests.post(Endpoints.REGISTER, json=payload)
    return response


@allure.step("Удаление пользователя")
def delete_user(access_token):
    """Удаление пользователя"""
    headers = {"Authorization": access_token}
    response = requests.delete(Endpoints.USER, headers=headers)
    return response


@allure.step("Авторизация пользователя")
def login_user(credentials):
    """Авторизация пользователя"""
    response = requests.post(Endpoints.LOGIN, json=credentials)
    return response


@allure.step("Изменение данных пользователя")
def update_user(access_token, update_data):
    """Изменение данных пользователя"""
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.patch(Endpoints.USER, headers=headers, json=update_data)
    return response


@allure.step("Создание заказа")
def create_order(access_token, ingredients_data):
    """Создание заказа"""
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.post(Endpoints.ORDERS, headers=headers, json=ingredients_data)
    return response


@allure.step("Получение заказов пользователя")
def get_user_orders(access_token):
    """Получение заказов пользователя"""
    headers = {"Authorization": access_token} if access_token else {}
    response = requests.get(Endpoints.ORDERS, headers=headers)
    return response


@allure.step("Получение access token из ответа")
def get_access_token_from_response(response):
    """Получение access token из ответа"""
    if response.status_code == 200 and "accessToken" in response.json():
        return response.json()["accessToken"]
    return None