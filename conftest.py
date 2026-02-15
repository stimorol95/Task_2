import pytest
import requests
from api.endpoints import Endpoints
from helpers.user_helper import register_user, delete_user, get_access_token_from_response
from data.test_data import Ingredients


@pytest.fixture
def registered_user():
    """Фикстура для создания и удаления пользователя"""
    response, payload = register_user()
    access_token = get_access_token_from_response(response)

    yield {
        "response": response,
        "payload": payload,
        "access_token": access_token
    }

    if access_token:
        delete_user(access_token)


@pytest.fixture
def auth_header(registered_user):
    """Фикстура для авторизационного заголовка"""
    access_token = registered_user["access_token"]
    return {"Authorization": access_token} if access_token else {}


@pytest.fixture
def existing_user():
    """Фикстура для создания пользователя, который уже существует"""
    payload = {
        "email": "preexisting_user@yandex.ru",
        "password": "securepass456",
        "name": "PreExisting"
    }

    response = requests.post(Endpoints.REGISTER, json=payload)

    access_token = None
    if response.status_code == 200:
        access_token = get_access_token_from_response(response)

    yield {
        "payload": payload,
        "access_token": access_token
    }

    if access_token:
        delete_user(access_token)


@pytest.fixture
def valid_ingredients():
    """Фикстура с валидными ингредиентами"""
    return {"ingredients": Ingredients.VALID_HASHES[:2]}


@pytest.fixture
def invalid_ingredients():
    """Фикстура с невалидным хешем ингредиента"""
    return {"ingredients": [Ingredients.INVALID_HASH]}