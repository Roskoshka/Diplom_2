import pytest
import requests

import helpers
from data import REGISTER_USER_BODY
from endpoints.user_api import UserApi
from urls import BASE_URL, DELETE_USER_ENDPOINT


# Фикстура - рандомные данные для создания пользователя в тесте и удаление этого пользователя в конце теста
@pytest.fixture(scope='function')
def default_user():
    payload = REGISTER_USER_BODY
    yield payload

    response = UserApi.login_user(payload)
    if response.status_code == 200:
        token = response.json()['accessToken']
        requests.delete(BASE_URL + DELETE_USER_ENDPOINT, headers={'authorization': token})
    else:
        pass


# Фикстура - получение токена авторизации после регистрации и авторизации рандомного пользователя
@pytest.fixture(scope='function')
def default_update_user(default_user):
    UserApi.register_user(default_user)
    login_body = helpers.get_login_user_data(default_user)
    response_login_user = UserApi.login_user(login_body)
    token = response_login_user.json()['accessToken']
    yield token

    requests.delete(BASE_URL + DELETE_USER_ENDPOINT, headers={'authorization': token})
