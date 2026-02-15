BASE_URL = "https://stellarburgers.education-services.ru"

class Endpoints:
    REGISTER = f"{BASE_URL}/api/auth/register"
    LOGIN = f"{BASE_URL}/api/auth/login"
    USER = f"{BASE_URL}/api/auth/user"
    LOGOUT = f"{BASE_URL}/api/auth/logout"
    TOKEN = f"{BASE_URL}/api/auth/token"
    ORDERS = f"{BASE_URL}/api/orders"
    ALL_ORDERS = f"{BASE_URL}/api/orders/all"
    INGREDIENTS = f"{BASE_URL}/api/ingredients"
    PASSWORD_RESET = f"{BASE_URL}/api/password-reset"
    PASSWORD_RESET_RESET = f"{BASE_URL}/api/password-reset/reset"