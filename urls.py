BASE_URL = 'https://stellarburgers.nomoreparties.site'

# User endpoints
# Регистрация пользователя POST
REGISTER_USER_ENDPOINT = '/api/auth/register'
# Авторизация пользователя POST
LOGIN_USER_ENDPOINT = '/api/auth/login'
# Удаление пользователя DELETE
DELETE_USER_ENDPOINT = '/api/auth/user'
# Получение данных о пользователе GET
GET_USER_ENDPOINT = '/api/auth/user'
# Обнолвение данных о пользователе PATCH
PATCH_USER_ENDPOINT = '/api/auth/user'
# Выход из системы POST
LOGOUT_USER_ENDPOINT = '/api/auth/logout'

# Order endpoints
# Создание заказа POST
CREATE_ORDER_ENDPOINT = '/api/orders'
# Создание заказа GET
GET_ORDERS_ENDPOINT = '/api/orders'
