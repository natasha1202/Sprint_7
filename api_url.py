class ApiUrl:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    LOGIN_API_URL = f'{BASE_URL}api/v1/courier/login'

    CREATE_COURIER_API_URL = f'{BASE_URL}api/v1/courier'

    DELETE_COURIER_API_URL = f'{BASE_URL}api/v1/courier/:id'

    COURIER_LIST_COUNT_API_URL = f'{BASE_URL}api/v1/courier/:id/ordersCount'

    FINISH_ORDER_API_URL = f'{BASE_URL}api/v1/orders/finish/:id'

    CANCEL_REQUEST_API_URL = f'{BASE_URL}api/v1/orders/cancel'

    LIST_ORDERS_API_URL = f'{BASE_URL}api/v1/orders'

    ORDER_TRACK_API_URL = f'{BASE_URL}api/v1/orders/track'

    ORDER_ACCEPT_API_URL = f'{BASE_URL}api/v1/orders/accept/:id'

    CREATE_ORDER_API_URL = f'{BASE_URL}api/v1/orders'

    UTILS_PING_SERVER_API_URL = f'{BASE_URL}api/v1/ping'

    STATION_SEARCH_API_URL = f'{BASE_URL}api/v1/stations/search'


