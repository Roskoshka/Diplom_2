import allure
import requests
import data
import urls


class UserApi:
    @staticmethod
    @allure.step("Запрос на создание пользователя")
    def register_user(body):
        return requests.post(urls.BASE_URL + urls.REGISTER_USER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Запрос на авторизацию пользователя")
    def login_user(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_USER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Запрос на обновление данных пользователя")
    def update_user(token):
        body = data.UPDATE_USER_BODY
        return requests.patch(urls.BASE_URL + urls.PATCH_USER_ENDPOINT, json=body,
                              headers={'authorization': token})

    @staticmethod
    @allure.step("Запрос на обновление данных пользователя уже имеющихся в системе (email)")
    def update_user_mail_of_already_registered_user(token):
        body = data.LOGIN_PASS_ALREADY_REGISTERED_USER
        return requests.patch(urls.BASE_URL + urls.PATCH_USER_ENDPOINT, json=body,
                              headers={'authorization': token})
