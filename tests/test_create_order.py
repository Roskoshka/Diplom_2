import allure
from pytest_check import check

import data
import helpers
from endpoints.order_api import OrderApi
from endpoints.user_api import UserApi


class TestCreateOrder:
    @allure.title('Успешный заказ авторизованного пользователя')
    @allure.description('Создание заказа под авторизованным пользователем, проверяем статус ответа и тело ответа')
    def test_create_order_authorized_user_success(self, default_user):
        body = helpers.get_modify_login_user_email(default_user)
        UserApi.login_user(body)
        response_create_order = OrderApi.create_order(data.CREATE_ORDER_BODY)

        assert response_create_order.status_code == 200
        with check:
            assert response_create_order.json()['success'] is True
        with check:
            assert response_create_order.json()['name'] == data.CREATE_ORDER_NAME

    @allure.title('Неуспешный заказ авторизованного пользователя с неверным хешем ингредиентов')
    @allure.description('Создание заказа с неверным хешем ингредиентов '
                        'под авторизованным пользователем, проверяем статус ответа')
    def test_create_order_with_invalid_ingredients_internal_server_error(self, default_user):
        body = helpers.get_modify_login_user_email(default_user)
        UserApi.login_user(body)
        response_create_order = OrderApi.create_order(data.CREATE_ORDER_WITH_INVALID_INGREDIENTS_BODY)

        assert (
                response_create_order.status_code == 500
                and data.INTERNAL_SERVER_ERROR in response_create_order.text
        )

    @allure.title('Неуспешный заказ авторизованного пользователя без ингридиентов')
    @allure.description('Создание заказа без ингридиентов под авторизованным пользователем, '
                        'проверяем статус ответа и тело ответа')
    def test_create_order_without_ingredients_bad_request(self, default_user):
        body = helpers.get_modify_login_user_email(default_user)
        UserApi.login_user(body)
        ingredients = {}
        response_create_order = OrderApi.create_order(ingredients)

        assert (
                response_create_order.status_code == 400
                and response_create_order.json()['success'] is False
                and response_create_order.json()['message'] == 'Ingredient ids must be provided'
        )

    @allure.title('Успешный заказ пользователя без авторизации')
    @allure.description('Создание заказа под неавторизованным пользователем, '
                        'проверяем статус ответа и тело ответа')
    def test_create_order_unauthorized_user_success(self):
        response_create_order = OrderApi.create_order(data.CREATE_ORDER_BODY)

        assert (
                response_create_order.status_code == 200
                and response_create_order.json()['success'] is True
                and response_create_order.json()['name'] == data.CREATE_ORDER_NAME
        )
