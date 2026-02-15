import requests
from api.endpoints import Endpoints
from data.test_data import UserData


def register_user(payload=None):
    """Регистрация нового пользователя"""
    if payload is None:
        payload = UserData.generate_user_payload()
    response = requests.post(Endpoints.REGISTER, json=payload)
    if response.status_code == 200:
        return response, payload
    return response, payload


def delete_user(access_token):
    """Удаление пользователя"""
    headers = {"Authorization": access_token}
    return requests.delete(Endpoints.USER, headers=headers)


def login_user(credentials):
    """Авторизация пользователя"""
    return requests.post(Endpoints.LOGIN, json=credentials)


def get_access_token_from_response(response):
    """Получение access token из ответа"""
    if response.status_code == 200 and "accessToken" in response.json():
        return response.json()["accessToken"]
    return None