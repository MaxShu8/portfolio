from requests import Response


class Checking():

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print(f'Проверка статус-кода --- УСПЕШНО! [ОР ---> {status_code} || ФР ---> {response.status_code}]')
        else:
            print(f'Ожидаемый статус-код: {status_code}\nФактический статус-код: {response.status_code}')
