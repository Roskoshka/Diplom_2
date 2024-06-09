import allure
import pytest

import data
from endpoints.user_api import UserApi


class TestRegisterUser:
    @allure.title('Успешная регистрация уникального пользователя')
    @allure.description('Создание пользователя, проверяем статус ответа и тело ответа')
    def test_register_user_success(self, default_user):
        response_register_user = UserApi.register_user(default_user)

        assert (
                response_register_user.status_code == 200
                and response_register_user.json()['success'] is True
                and response_register_user.json()["user"] is not None
        )

    @allure.title('Регистрация пользователя, который уже зарегистрирован')
    @allure.description('Создаем пользователя, который уже зарегистрирован, проверям статус ответа и тело ответа')
    def test_register_user_already_registered_forbidden(self, default_user):
        UserApi.register_user(default_user)
        response_register_user_already_registered = UserApi.register_user(default_user)

        assert (
                response_register_user_already_registered.status_code == 403
                and response_register_user_already_registered.json()['success'] is False
                and response_register_user_already_registered.json()['message'] == data.USER_ALREADY_EXISTS
        )

    @allure.title('Ошибка при регистрации пользователя без одного из обязательных параметров')
    @allure.description('Проверяем регистрацию пользователя, когда не заполнено одно из обязательных полей')
    @pytest.mark.parametrize("body", [data.REGISTER_USER_BODY_WITHOUT_EMAIL,
                                      data.REGISTER_USER_BODY_WITH_EMPTY_EMAIL,
                                      data.REGISTER_USER_BODY_WITHOUT_PASSWORD,
                                      data.REGISTER_USER_BODY_WITH_EMPTY_PASSWORD,
                                      data.REGISTER_USER_BODY_WITHOUT_NAME,
                                      data.REGISTER_USER_BODY_WITH_EMPTY_NAME])
    def test_register_user_with_empty_required_field_forbidden(self, body):
        response_register_user_with_empty_required_field = UserApi.register_user(body)

        assert (
                response_register_user_with_empty_required_field.status_code == 403
                and response_register_user_with_empty_required_field.json()['success'] is False
                and response_register_user_with_empty_required_field.json()['message'] ==
                data.ERROR_REQUIRED_FIELDS
        )