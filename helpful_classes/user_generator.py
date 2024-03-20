import allure
import requests

from helpful_classes.helper import Helper


class UserGenerator:
    @staticmethod
    @allure.step('Генерируется новый зарегистрированный курьер')
    def register_new_courier_and_return_login_password():
        login_pass = []

        login = Helper.generate_random_string(15)
        password = Helper.generate_random_string(15)
        first_name = Helper.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass
