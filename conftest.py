import random
import datetime as dt

import pytest

from helpful_classes.helper import Helper


@pytest.fixture(scope='function')
def order():
    first_name = Helper.generate_random_string(14)
    last_name = Helper.generate_random_string(14)
    address = f'{Helper.generate_random_string(10)} {random.randint(1, 100)}'
    metro_station = random.randint(4, 100)
    phone = f'+7{random.randint(1000000000, 9999999999)}'
    rent_time = random.randint(1, 10)

    time_delta = random.randint(1, 10)
    future_date = dt.date.today() + dt.timedelta(days=time_delta)
    delivery_date = future_date.strftime("%Y-%m-%d")
    comment = Helper.generate_random_string(20)
    return {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment
    }
