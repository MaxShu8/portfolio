import json

import requests
from utils.logger_google_loocation import Logger


class Test_location():
    """Создание, изменение и удаление локации."""

    def test_create_new_location(self):

        """---------Создание локации (метод POST)--------"""

        base_url = 'https://rahulshettyacademy.com'
        resource_post = '/maps/api/place/add/json'
        params = '?key=qaclick123'

        print('\n\033[1;33m---------Создание локации (метод POST)---------\033[0;0m')
        url_post = base_url + resource_post + params
        print(url_post)

        json_post = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        Logger.add_request_data(url_post, method='POST')
        response_post = requests.post(url_post, json=json_post)
        Logger.add_response_data(response_post)
        print(response_post.text)

        assert response_post.status_code == 200
        if response_post.status_code == 200:
            print(f'\033[0;42m Проверка статус-кода --- УСПЕШНО!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_post.status_code}]')
        else:
            print(f'\033[0;41m Проверка статус-кода --- ПРОВАЛ!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_post.status_code}]')

        check = response_post.json()
        place_id = check.get('place_id')

        json_response = json.loads(response_post.text)
        if list(json_response) == ['status', 'place_id', 'scope', 'reference', 'id']:
            print(f'\033[0;42m Проверка структуры ответа --- УСПЕШНО!\033[0;0m [Все обязательные поля ответа присутствуют]')
        else:
            print(f'\033[0;41m Проверка наличия полей --- ПРОВАЛ!\033[0;0m [Структура ответа не соответствует]')

        """---------Запрашиваем информацию о созданной локации (метод GET)--------"""

        resource_get = '/maps/api/place/get/json'

        print('\n\033[1;33m---------Запрос информации о созданной локации (метод GET)---------\033[0;0m')
        url_get = base_url + resource_get + params + '&place_id=' + place_id
        print(url_get)

        Logger.add_request_data(url_get, method='GET')
        response_get = requests.get(url_get)
        Logger.add_response_data(response_get)
        print(response_get.text)

        assert response_get.status_code == 200
        if response_get.status_code == 200:
            print(f'\033[0;42m Проверка статус-кода --- УСПЕШНО!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_get.status_code}]')
        else:
            print(f'\033[0;41m Проверка статус-кода --- ПРОВАЛ!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_get.status_code}]')

        json_response = json.loads(response_get.text)
        if list(json_response) == ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']:
            print(f'\033[0;42m Проверка структуры ответа --- УСПЕШНО!\033[0;0m [Все обязательные поля ответа присутствуют]')
        else:
            print(f'\033[0;41m Проверка наличия полей --- ПРОВАЛ!\033[0;0m [Структура ответа не соответствует]')

        """---------Изменение локации (метод PUT)--------"""

        resource_post = '/maps/api/place/update/json'

        print('\n\033[1;33m---------Изменение локации (метод PUT)---------\033[0;0m')
        url_put = base_url + resource_post + params
        print(url_put)

        json_put = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        Logger.add_request_data(url_put, method='PUT')
        response_put = requests.put(url_put, json=json_put)
        Logger.add_response_data(response_put)
        print(response_put.text)

        assert response_put.status_code == 200
        if response_put.status_code == 200:
            print(f'\033[0;42m Проверка статус-кода --- УСПЕШНО!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_put.status_code}]')
        else:
            print(f'\033[0;41m Проверка статус-кода --- ПРОВАЛ!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_put.status_code}]')

        json_response = json.loads(response_put.text)
        if list(json_response) == ['msg']:
            print(f'\033[0;42m Проверка структуры ответа --- УСПЕШНО!\033[0;0m [Все обязательные поля ответа присутствуют]')
        else:
            print(f'\033[0;41m Проверка наличия полей --- ПРОВАЛ!\033[0;0m [Структура ответа не соответствует]')

        """---------Запрашиваем информацию об измененной локации (метод GET)--------"""

        print('\n\033[1;33m---------Запрос информации об измененной локации (метод GET)---------\033[0;0m')
        url_get = base_url + resource_get + params + '&place_id=' + place_id
        print(url_get)

        Logger.add_request_data(url_get, method='GET')
        response_get = requests.get(url_get)
        Logger.add_response_data(response_get)
        print(response_get.text)

        assert response_get.status_code == 200
        if response_get.status_code == 200:
            print(f'\033[0;42m Проверка статус-кода --- УСПЕШНО!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_get.status_code}]')
        else:
            print(f'\033[0;41m Проверка статус-кода --- ПРОВАЛ!\033[0;0m' f' [ОР ---> 200 || ФР ---> {response_get.status_code}]')

        json_response = json.loads(response_get.text)
        need_list = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        assert list(json_response) == need_list
        if list(json_response) == need_list:
            print(f'\033[0;42m Проверка структуры ответа --- УСПЕШНО!\033[0;0m [Все обязательные поля ответа присутствуют]')
        else:
            print(f'\033[0;41m Проверка наличия полей --- ПРОВАЛ!\033[0;0m [Структура ответа не соответствует]')


