import string

import requests

from api_url import ApiUrl
from helpful_classes.assertions import Assertions
import random


class Helper:

    @staticmethod
    def calculate_url(url, user_id):
        url_with_id = url.replace('{id}', user_id)
        return url_with_id

    @staticmethod
    def generate_courier_data():

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = Helper.generate_random_string(15)
        password = Helper.generate_random_string(15)
        first_name = Helper.generate_random_string(10)

        data = {
            'login': login,
            'password': password,
            'first_name': first_name
        }
        return data

    @staticmethod
    def generate_data():
        new_courier = Helper.generate_courier_data()
        data = {'login': new_courier.get('login'), 'password': new_courier.get('password')}
        return data


    @staticmethod
    def delete_courier(url, current_id):
        str_id = str(current_id)
        current_url = url.replace(':id', str_id)
        response = requests.delete(current_url)
        Assertions.assert_code_status(response, 200)


    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def set_data_with_none(courier, number):
        if number == 0:
            login = courier[0]
            password = None
        else:
            login = None
            password = courier[1]

        return {'login': login, 'password': password}

    @staticmethod
    def set_data_with_random_value(courier, number):
        if number == 0:
            login = courier[0]
            password = Helper.generate_random_string(8)
        else:
            login = Helper.generate_random_string(8)
            password = courier[1]

        return {'login': login, 'password': password}



if __name__ == "__main__":
    Helper.delete_courier(ApiUrl.DELETE_COURIER_API_URL, 277727)
