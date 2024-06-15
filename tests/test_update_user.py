import allure

import data
from endpoints.user_api import UserApi


class TestUpdateUser:
    @allure.title('Обновление авторизованного пользователя')
    @allure.description('Проверка успешного обновления данных пользователя. Проверяем статус ответа и тело ответа')
    def test_update_authorized_user_success(self, default_update_user):
        response_update_user = UserApi.update_user(default_update_user)

        assert (
                response_update_user.status_code == 200
                and response_update_user.json()['success'] is True
                and response_update_user.json()['user']['email'] == data.UPDATE_USER_BODY.get('email')
                and response_update_user.json()['user']['name'] == data.UPDATE_USER_BODY.get('name')
        )

    @allure.title('Обновление неавторизованного пользователя')
    @allure.description('Проверка неуспешного обновления данных неавторизованного пользователя.'
                        'Проверяем статус ответа и тело ответа')
    def test_update_unauthorized_user_unauthorized(self):
        token = ""
        response_update_user = UserApi.update_user(token)

        assert (
                response_update_user.status_code == 401
                and response_update_user.json()['success'] is False
                and response_update_user.json()['message'] == data.UNAUTHORIZED_ERROR
        )

    @allure.title('Обновление авторизованного пользователя. Изменение email на уже существующий в системе')
    @allure.description('Проверка неуспешного обновления данных пользователя '
                        'при изменении email на уже существующий в системе. Проверяем статус ответа и тело ответа')
    def test_update_auth_user_mail_of_already_registered_user(self, default_update_user):
        response_update_user = UserApi.update_user_mail_of_already_registered_user(default_update_user)

        assert (
                response_update_user.status_code == 403
                and response_update_user.json()['success'] is False
                and response_update_user.json()['message'] == data.SUCH_EMAIL_ALREADY_EXISTS
        )
