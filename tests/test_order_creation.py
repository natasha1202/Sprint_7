import allure
import pytest
import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions


class TestOrderCreation:

    @pytest.mark.parametrize("color",
                             [
                                 "BLACK",
                                 "GREY",
                                 ("BLACK", "GREY"),
                                 None
                              ]
                             )
    @allure.title("Тест проверяет создание заказа. Позитивный сценарий")
    @allure.description("Тест проверяет, что можно создать заказ с разными цветами")
    def test_order_creation_success(self, order, color):
        data = {
            "firstName": order.get('first_name'),
            "lastName": order.get('last_name'),
            "address": order.get('address'),
            "metroStation": order.get('metro_station'),
            "phone": order.get('phone'),
            "rentTime": order.get('rent_time'),
            "deliveryDate": order.get('delivery_date'),
            "comment": order.get('comment'),
            "color": color
        }

        response = requests.post(ApiUrl.CREATE_ORDER_API_URL, data=data)

        Assertions.assert_code_status(response, 201)
        Assertions.assert_json_has_key(response, 'track')
