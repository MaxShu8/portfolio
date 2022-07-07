import os
import datetime as dt
from requests import Response


class Logger():
    file_name = f"logs/log_{dt.datetime.now().strftime('%d-%m-%y %H-%M-%S')}.log"

    @classmethod
    def write_data(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as file_data:
            file_data.write(data)

    @classmethod
    def add_request_data(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        add_data = f'\n-----\n'
        add_data += f'Test: {test_name}\n'
        add_data += f'Time: {dt.datetime.now()}\n'
        add_data += f'Request method: {method}\n'
        add_data += f'Request URL: {url}\n'

        cls.write_data(add_data)

    @classmethod
    def add_response_data(cls, result: Response):
        headers_info = dict(result.headers)

        add_data = f'Response code: {result.status_code}\n'
        add_data += f'Response text: {result.text}\n'
        add_data += f'Response headers: {headers_info}\n'
        add_data += f'\n-----\n'

        cls.write_data(add_data)


