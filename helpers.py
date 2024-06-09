import allure
import data
from endpoints.user_api import UserApi


@allure.step("Получение тела запроса для авторизации зарегистрированного пользователя")
def get_login_user_data(body):
    UserApi.register_user(body)
    auth_email = body.get('email')
    auth_password = body.get('password')
    auth_body = {'email': auth_email, 'password': auth_password}
    return auth_body


@allure.step("Получение тела запроса для авторизации зарегистрированного пользователя с невалидным email")
def get_modify_login_user_email(body):
    UserApi.register_user(body)
    auth_email = data.fake.email()
    auth_password = body.get('password')
    auth_body = {'email': auth_email, 'password': auth_password}
    return auth_body


@allure.step("Получение тела запроса для авторизации зарегистрированного пользователя без email")
def get_modify_login_user_password(body):
    UserApi.register_user(body)
    auth_email = body.get('email')
    auth_password = data.fake.password()
    auth_body = {'email': auth_email, 'password': auth_password}
    return auth_body


@allure.step("Получение тела запроса для авторизации зарегистрированного пользователя без email")
def get_modify_login_user_without_email(body):
    UserApi.register_user(body)
    auth_password = body.get('password')
    auth_body = {'password': auth_password}
    return auth_body


@allure.step("Получение тела запроса для авторизации зарегистрированного пользователя без password")
def get_modify_login_user_without_password(body):
    UserApi.register_user(body)
    auth_email = body.get('email')
    auth_body = {'email': auth_email}
    return auth_body

