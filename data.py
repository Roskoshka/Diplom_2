from faker import Faker

fake = Faker()

# Тело запроса для регистрации уникального пользователя
REGISTER_USER_BODY = {
                    "email": fake.email(),
                    "password": fake.password(),
                    "name": fake.name()
                    }

# Тело запроса для регистрации пользователя без email
REGISTER_USER_BODY_WITHOUT_EMAIL = {
                    "password": fake.password(),
                    "name": fake.name()
                    }

# Тело запроса для регистрации пользователя с пустым email
REGISTER_USER_BODY_WITH_EMPTY_EMAIL = {
                    "email": "",
                    "password": fake.password(),
                    "name": fake.name()
                    }

# Тело запроса для регистрации пользователя без password
REGISTER_USER_BODY_WITHOUT_PASSWORD = {
                    "email": fake.email(),
                    "name": fake.name()
                    }

# Тело запроса для регистрации пользователя с пустым password
REGISTER_USER_BODY_WITH_EMPTY_PASSWORD = {
                    "email": fake.email(),
                    "password": "",
                    "name": fake.name()
                    }

# Тело запроса для регистрации пользователя без name
REGISTER_USER_BODY_WITHOUT_NAME = {
                    "email": fake.email(),
                    "password": fake.password()
                    }

# Тело запроса для регистрации пользователя с пустым name
REGISTER_USER_BODY_WITH_EMPTY_NAME = {
                    "email": fake.email(),
                    "password": fake.password(),
                    "name": ""
                    }

# Тело запроса для обновления данных пользователя - name
UPDATE_USER_BODY = {
                    "email": fake.email(),
                    "name": fake.name()
                    }

# Данные уже зарегистрированного пользователя
LOGIN_PASS_ALREADY_REGISTERED_USER = {
                    "email": 'alenakalinovskaya7999@gmail.com',
                    "password": '123456'
                    }

# Данные для создания заказа
CREATE_ORDER_BODY = {'ingredients': ["61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa71",
                                     "61c0c5a71d1f82001bdaaa6d"]}

# Данные для проверки созданного заказа
CREATE_ORDER_NAME = 'Spicy био-марсианский флюоресцентный бургер'

CREATE_ORDER_WITH_INVALID_INGREDIENTS_BODY = {'ingredients': ['61c0c5a71d1f82001bdaaa721', '609646e4dc916e35776b2870']}

# Ответы с сервера
UNAUTHORIZED_ERROR = 'You should be authorised'
INTERNAL_SERVER_ERROR = 'Internal Server Error'
SUCH_EMAIL_ALREADY_EXISTS = 'User with such email already exists'
EMAIL_PASSWORD_INCORRECT = 'email or password are incorrect'
USER_ALREADY_EXISTS = 'User already exists'
ERROR_REQUIRED_FIELDS = 'Email, password and name are required fields'
