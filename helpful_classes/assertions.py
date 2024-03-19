import allure
from requests import Response
import json


class Assertions:
    @staticmethod
    @allure.step('Проверка значения в JSON по ключу')
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does not have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    @allure.step('Проверка наличия ключа в JSON')
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does not have key '{name}'"

    @staticmethod
    @allure.step('Проверка статус-кода ответа')
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    @allure.step('Проверка сообщения в ответе')
    def assert_content_message(response: Response, expected_error_message):
        content = response.content.decode("utf-8")
        assert content == expected_error_message, \
            f"Unexpected error message! Expected: {expected_error_message}\n"\
            f"Actual message {content}"






