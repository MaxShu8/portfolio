import requests
from utils.logger_petshop import Logger


class Http_methods():
    headers = {'Content-Type': 'application/json'}

    @staticmethod
    def get(url):
        Logger.request_data(url, 'GET')
        result = requests.get(url, headers=Http_methods.headers)
        Logger.response_data(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.request_data(url, 'POST')
        result = requests.post(url, json=body, headers=Http_methods.headers)
        Logger.response_data(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.request_data(url, 'PUT')
        result = requests.put(url, json=body, headers=Http_methods.headers)
        Logger.response_data(result)
        return result

    @staticmethod
    def delete(url):
        Logger.request_data(url, 'DELETE')
        result = requests.delete(url, headers=Http_methods.headers)
        Logger.response_data(result)
        return result

