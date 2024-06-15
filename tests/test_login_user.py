import allure
import helpers
import data
from endpoints.user_api import UserApi
from conftest import default_user


class TestLoginUser:
    @allure.title('Успешный логин пользователя')
    @allure.description('Проверка успешного логина пользователя. Проверяем статус ответа и тело ответа')
    def test_login_user_success(self, default_user):
        body = helpers.get_login_user_data(default_user)
        response_login_user = UserApi.login_user(body)

        assert (
                response_login_user.status_code == 200
                and response_login_user.json()['success'] is True
                and response_login_user.json()["user"] is not None
        )

    @allure.title('Неуспешный логин пользователя с невалидным email')
    @allure.description('Проверка неуспешного логина пользователя, '
                        'если email неверный')
    def test_login_user_with_invalid_email_unauthorized(self, default_user):
        body = helpers.get_modify_login_user_email(default_user)
        response_login_user = UserApi.login_user(body)

        assert (
                response_login_user.status_code == 401
                and response_login_user.json()['success'] is False
                and response_login_user.json()["message"] ==
                data.EMAIL_PASSWORD_INCORRECT
        )

    @allure.title('Неуспешный логин пользователя с невалидным password')
    @allure.description('Проверка неуспешного логина пользователя, '
                        'если password неверный')
    def test_login_user_with_invalid_password_unauthorized(self, default_user):
        body = helpers.get_modify_login_user_password(default_user)
        response_login_user = UserApi.login_user(body)

        assert (
                response_login_user.status_code == 401
                and response_login_user.json()['success'] is False
                and response_login_user.json()["message"] ==
                data.EMAIL_PASSWORD_INCORRECT
        )

    @allure.title('Неуспешный логин пользователя без email')
    @allure.description('Проверка неуспешного логина пользователя, '
                        'если email отсутствует в теле запроса')
    def test_login_user_without_email_unauthorized(self, default_user):
        body = helpers.get_modify_login_user_without_email(default_user)
        response_login_user = UserApi.login_user(body)

        assert (
                response_login_user.status_code == 401
                and response_login_user.json()['success'] is False
                and response_login_user.json()["message"] ==
                data.EMAIL_PASSWORD_INCORRECT
        )

    @allure.title('Неуспешный логин пользователя без password')
    @allure.description('Проверка неуспешного логина пользователя, '
                        'если password отсутствует в теле запроса')
    def test_login_user_without_password_unauthorized(self, default_user):
        body = helpers.get_modify_login_user_without_password(default_user)
        response_login_user = UserApi.login_user(body)

        assert (
                response_login_user.status_code == 401
                and response_login_user.json()['success'] is False
                and response_login_user.json()["message"] ==
                data.EMAIL_PASSWORD_INCORRECT
        )
