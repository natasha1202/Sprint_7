import string
import random

import allure
import requests


class Helper:

    @staticmethod
    @allure.step('Генерируется ссылка с id пользователя')
    def calculate_url(url, user_id):
        url_with_id = url.replace('{id}', user_id)
        return url_with_id

    @staticmethod
    @allure.step('Генерируется ссылка с id пользователя')
    def generate_courier_data():
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
    @allure.step('Генерируются пара логин-пароль для нового курьера')
    def generate_data():
        new_courier = Helper.generate_courier_data()
        data = {'login': new_courier.get('login'), 'password': new_courier.get('password')}
        return data

    @staticmethod
    @allure.step('Удаление курьера по id')
    def delete_courier(url, current_id):
        str_id = str(current_id)
        current_url = url.replace(':id', str_id)
        response = requests.delete(current_url)

    @staticmethod
    @allure.step('Генерация произвольной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Создание для существующего курьера пары логин-пароль, в которой одно из полей пустое')
    def set_data_with_none(courier, number):
        if number == 0:
            login = courier[0]
            password = None
        else:
            login = None
            password = courier[1]

        return {'login': login, 'password': password}

    @staticmethod
    @allure.step('Создание для существующего курьера пары логин-пароль, в которой одно '
                 'из полей заполнено произвольным значением')
    def set_data_with_random_value(courier, number):
        if number == 0:
            login = courier[0]
            password = Helper.generate_random_string(8)
        else:
            login = Helper.generate_random_string(8)
            password = courier[1]

        return {'login': login, 'password': password}


