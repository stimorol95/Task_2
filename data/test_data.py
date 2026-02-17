import random
import string


class UserMessages:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    INCORRECT_LOGIN = "email or password are incorrect"
    UNAUTHORIZED = "You should be authorised"
    EMAIL_EXISTS = "User with such email already exists"
    INGREDIENTS_REQUIRED = "Ingredient ids must be provided"


class Ingredients:
    VALID_HASHES = [
        "61c0c5a71d1f82001bdaaa6d",  # Краторная булка
        "61c0c5a71d1f82001bdaaa6f",  # Мясо бессмертных моллюсков
        "61c0c5a71d1f82001bdaaa70",  # Соус Spicy-X
    ]
    INVALID_HASH = "invalid_hash_12345"
    
    VALID_INGREDIENTS_REQUEST = {"ingredients": VALID_HASHES[:2]}
    INVALID_INGREDIENTS_REQUEST = {"ingredients": [INVALID_HASH]}
    EMPTY_INGREDIENTS_REQUEST = {"ingredients": []}


class UserData:
    @staticmethod
    def generate_unique_user():
        """Генерация данных уникального пользователя"""
        email = f"testuser_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@yandex.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        name = f"TestUser_{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}"
        return {
            "email": email,
            "password": password,
            "name": name
        }

    @staticmethod
    def generate_unique_email():
        """Генерация уникального email"""
        return f"update_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@yandex.ru"

    @staticmethod
    def generate_unique_name():
        """Генерация уникального имени"""
        return f"UpdatedName_{''.join(random.choices(string.ascii_uppercase + string.digits, k=4))}"

    # Фиксированные тестовые данные для существующего пользователя
    EXISTING_USER = {
        "email": "test_user_exists@yandex.ru",
        "password": "password123",
        "name": "TestUser"
    }

    # Данные для негативных проверок
    INVALID_CREDENTIALS = {
        "email": "wrong@email.com",
        "password": "wrongpass"
    }

    MISSING_FIELDS = [
        {"password": "password123", "name": "NoEmail"},
        {"email": "no_pass@yandex.ru", "name": "NoPass"},
        {"email": "no_name@yandex.ru", "password": "pass"}
    ]