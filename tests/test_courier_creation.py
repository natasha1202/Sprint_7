import allure
import pytest
import requests

from api_url import ApiUrl
from helpful_classes.helper import Helper
from helpful_classes.assertions import Assertions
from helpful_classes.user_generator import UserGenerator


@allure.epic("Создание курьера")
class TestCourierCreation:

    @allure.description('Создание курьера. Позитивный сценарий')
    def test_courier_creation_positive(self):
        new_courier = Helper.generate_courier_data()
        payload = {'login': new_courier.get('login'),
                   'password': new_courier.get('password')
                   }

        response = requests.post(ApiUrl.CREATE_COURIER_API_URL, data=payload)
        Assertions.assert_code_status(response, 201)
        Assertions.assert_content_message(response, '{"ok":true}')

        response_login = requests.post(ApiUrl.LOGIN_API_URL, data=payload)
        courier_id = response_login.json()['id']
        Helper.delete_courier(ApiUrl.DELETE_COURIER_API_URL,courier_id)

    @allure.description('Сохдание курьера с уже существующими данными')
    def test_create_duplicate_courier(self):
        new_courier = UserGenerator.register_new_courier_and_return_login_password()
        payload = {'login': new_courier[0],
                   'password': new_courier[1],
                   'first_name': new_courier[2]
                   }
        response = requests.post(ApiUrl.CREATE_COURIER_API_URL, data=payload)
        Assertions.assert_code_status(response, 409)
        Assertions.assert_json_value_by_name(response,
                                             'message',
                                             'Этот логин уже используется',
                                             f'Неверное сообщение об ошибке - {response.json()['message']}'
                                             )

    @pytest.mark.parametrize("login, password, first_name",
                             [
                                 (
                                      Helper.generate_courier_data().get('login'),
                                      None,
                                      Helper.generate_courier_data().get('first_name')
                                 ),
                                 (
                                      None,
                                      Helper.generate_courier_data().get('password'),
                                      Helper.generate_courier_data().get('first_name')
                                 ),
                                 (
                                     Helper.generate_courier_data().get('login'),
                                     Helper.generate_courier_data().get('password'),
                                     None
                                 )
                              ]
                             )
    @allure.description('Тест проверяет, что если хотя бы одно из полей не заполнено при создании, '
                        'то курьер не создается')
    def test_create_courier_not_all_mandatory_fields_filled(self, login, password, first_name):
        payload = {'login': login, 'password': password, 'first_name': first_name}
        print(payload)
        response = requests.post(ApiUrl.CREATE_COURIER_API_URL, data=payload)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_json_value_by_name(response,
                                             'message',
                                             'Недостаточно данных для создания учетной записи',
                                             f'Неверное сообщение об ошибке - {response.json()['message']}')

