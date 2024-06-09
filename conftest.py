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
    token = response.json()['accessToken']
    requests.delete(BASE_URL + DELETE_USER_ENDPOINT, headers={'authorization': token})

# Фикстура - получение токена авторизации после регистрации и авторизации рандомного пользователя
@pytest.fixture(scope='function')
def default_update_user():
    payload = REGISTER_USER_BODY
    UserApi.register_user(payload)
    login_body = helpers.get_login_user_data(payload)
    response_login_user = UserApi.login_user(login_body)
    token = response_login_user.json()['accessToken']
    yield token

    requests.delete(BASE_URL + DELETE_USER_ENDPOINT, headers={'authorization': token})
