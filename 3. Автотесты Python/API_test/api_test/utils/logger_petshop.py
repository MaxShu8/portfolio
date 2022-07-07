from requests import Response
import datetime as dt
import os


class Logger():

    file_name = f"logs/log_{dt.datetime.now().strftime('%d-%m-%y  %H-%M-%S')}.log"

    @classmethod
    def write_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as log_file:
            log_file.write(data)

    @classmethod
    def request_data(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {dt.datetime.now()}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += '\n'
        cls.write_file(data_to_add)

    @classmethod
    def response_data(cls, result: Response):
        headers_info = dict(result.headers)

        data_to_add = f'Response code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers_info}\n'
        data_to_add += f'\n-----\n'
        cls.write_file(data_to_add)
