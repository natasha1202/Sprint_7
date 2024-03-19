import allure
import pytest
import requests

from helpful_classes.helper import Helper
from api_url import ApiUrl
from helpful_classes.assertions import Assertions
from helpful_classes.user_generator import UserGenerator


@allure.epic("Логин курьера в системе")
class TestCourierLogin:

    @allure.title("Тест проверяет авторизацию существующего курьера. Позитивный сценарий")
    @allure.description("Тест проверяет. что зарегистированный курьер может успешно зайти в систему "
                        "и в ответе будет возвращен id клиента")
    def test_courier_login_with_correct_credentials(self):
        new_courier = UserGenerator.register_new_courier_and_return_login_password()
        payload = {
            'login': new_courier[0],
            'password': new_courier[1]
        }

        response = requests.post(ApiUrl.LOGIN_API_URL, data=payload)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

        courier_id = response.json()['id']
        Helper.delete_courier(ApiUrl.DELETE_COURIER_API_URL, courier_id)

    @pytest.mark.parametrize("courier, data_flag",
                             [
                                 (UserGenerator.register_new_courier_and_return_login_password(), 0),
                                 (UserGenerator.register_new_courier_and_return_login_password(), 1)
                              ]
                             )
    @allure.title("Авторизацию с незаполненным обязательным полем")
    @allure.description("Тест проверяет, что если хотя бы одно поле не заполнено, но авторизация не проходит "
                        "Происходит проверка сообщения об ошибке")
    def test_courier_login_without_login_or_pwd(self, courier, data_flag):
        data = Helper.set_data_with_none(courier, data_flag)

        response = requests.post(ApiUrl.LOGIN_API_URL, data=data)
        Assertions.assert_code_status(response, 404)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'Недостаточно данных для входа',
            'Неверное сообщение об ошибке')

        login_data = {'login': courier[0], 'password': courier[1]}
        response1 = requests.post(ApiUrl.LOGIN_API_URL, data=login_data)
        courier_id = response1.json()['id']
        Helper.delete_courier(ApiUrl.DELETE_COURIER_API_URL, courier_id)

    @pytest.mark.parametrize("courier, data_flag",
                             [
                                 (UserGenerator.register_new_courier_and_return_login_password(), 0),
                                 (UserGenerator.register_new_courier_and_return_login_password(), 1)
                              ]
                             )
    @allure.title("Авторизацию с неверно заполненным логином или паролем")
    @allure.description("Тест проверяет авторизацию с неверно заполненным логином или паролем, "
                        "Авторизация отклоняется и происходит проверка сообщения об ошибке")
    def test_courier_login_with_wrong_login_or_pwd(self, courier, data_flag):
        data = Helper.set_data_with_random_value(courier, data_flag)

        response = requests.post(ApiUrl.LOGIN_API_URL, data=data)
        Assertions.assert_code_status(response, 404)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'Учетная запись не найдена',
            'Неверное сообщение об ошибке')

        login_data = {'login': courier[0], 'password': courier[1]}
        response1 = requests.post(ApiUrl.LOGIN_API_URL, data=login_data)
        courier_id = response1.json()['id']
        Helper.delete_courier(ApiUrl.DELETE_COURIER_API_URL, courier_id)

    @allure.title("Тест проверяет авторизацию незарегистрированного курьера")
    @allure.description("Тест проверяет, что незарегистрированный курьер не может авторизоваться в системе "
                        "Происходит проверка сообщения об ошибке")
    def test_courier_login_with_correct_credentials_not_registred_courier(self):
        new_courier = Helper.generate_courier_data()
        data = {
            'login': new_courier.get('login'),
            'password': new_courier.get('password')
        }
        response = requests.post(ApiUrl.LOGIN_API_URL, data=data)

        Assertions.assert_code_status(response, 404)
        Assertions.assert_json_value_by_name(
            response,
            'message',
            'Учетная запись не найдена',
            'Неверное сообщение об ошибке')
