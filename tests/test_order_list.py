import random

import allure
import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions


class TestOrderList:

    @allure.title("Тест проверяет, что метод возвращает список заказов")
    @allure.description("Происходит запрос списка заказов в системе с параметром limit количества заказов")
    def test_get_order_list(self):
        params = {'limit': random.randint(1,3)}
        response = requests.get(ApiUrl.LIST_ORDERS_API_URL, params=params, timeout=(10, 30))

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'orders')
