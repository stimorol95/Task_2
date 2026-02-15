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
    EMPTY_LIST = []


class UserData:
    @staticmethod
    def generate_user_payload():
        email = f"testuser_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@yandex.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        name = f"TestUser_{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}"

        return {
            "email": email,
            "password": password,
            "name": name
        }

    EXISTING_USER = {
        "email": "existing_user@yandex.ru",
        "password": "password123",
        "name": "ExistingUser"
    }

    INVALID_CREDENTIALS = {
        "email": "wrong@email.com",
        "password": "wrongpass"
    }

    MISSING_FIELDS = [
        {"password": "password123", "name": "NoEmail"},  # Missing email
        {"email": "no_pass@yandex.ru", "name": "NoPass"},  # Missing password
        {"email": "no_name@yandex.ru", "password": "password123"}  # Missing name
    ]

    UPDATE_FIELDS = [
        {"email": "updated_email@yandex.ru"},
        {"name": "UpdatedName"},
        {"email": "another_email@yandex.ru", "name": "AnotherName"}
    ]