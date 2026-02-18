import random
import string


class UserGenerator:
    """Генераторы тестовых данных для пользователей"""
    @staticmethod
    def generate_unique_email():
        """Генерация уникального email"""
        return f"update_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@yandex.ru"

    @staticmethod
    def generate_unique_name():
        """Генерация уникального имени"""
        return f"UpdatedName_{''.join(random.choices(string.ascii_uppercase + string.digits, k=4))}"

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