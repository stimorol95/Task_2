import pytest
import requests
from api.endpoints import Endpoints
from helpers.user_helper import register_user, delete_user, get_access_token_from_response
from data.test_data import UserData


@pytest.fixture
def created_user():
    """
    Фикстура создает уникального пользователя перед тестом
    и удаляет его после теста.
    """
    user_data = UserData.generate_unique_user()
    response = register_user(user_data)
    access_token = get_access_token_from_response(response)
    
    yield {
        "payload": user_data,
        "response": response,
        "access_token": access_token
    }
    
    if access_token:
        delete_user(access_token)


@pytest.fixture
def existing_user_credentials():
    """
    Фикстура гарантирует, что пользователь существует в системе,
    но не создает его заново при каждом вызове.
    """
    # Проверяем, существует ли пользователь
    response = requests.post(Endpoints.LOGIN, json=UserData.EXISTING_USER)
    # Если пользователя нет, создаем его ОДИН раз
    if response.status_code != 200:
        register_user(UserData.EXISTING_USER)
    # Возвращаем только credentials, без создания в фикстуре
    return {
        "email": UserData.EXISTING_USER["email"],
        "password": UserData.EXISTING_USER["password"]
    }