import allure
import requests

import urls


class OrderApi:
    @staticmethod
    @allure.step("Запрос на создание заказа")
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Запрос на получение списка заказов")
    def get_orders(token):
        return requests.get(urls.BASE_URL + urls.GET_ORDERS_ENDPOINT, headers={'authorization': token})
