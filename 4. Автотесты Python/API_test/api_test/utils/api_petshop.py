from utils.http_methods_for_petshop import Http_methods


base_url = 'https://petstore.swagger.io/v2'
resource = '/user/'
username = 'Neo'
change_username = 'Petya'


class Create_new_user():

    @staticmethod
    def create_new_user():    # Создаем нового пользователя методом POST

        post_body = {
            "id": 8,
            "username": username,
            "firstName": "Ivan",
            "lastName": "Ivanov",
            "email": "fortesting@gmail.com",
            "password": "1234",
            "phone": "88001112233",
            "userStatus": 0
        }

        url_post = base_url + resource
        print(url_post)
        response_post = Http_methods.post(url_post, post_body)
        print(response_post.text)
        return response_post

    @staticmethod
    def info_about_user():    # Запрашиваем информацию о созданном пользователе методом GET

        url_get = base_url + resource + username
        print(url_get)
        response_get = Http_methods.get(url_get)
        print(response_get.text)
        return response_get

    @staticmethod
    def update_user():    # Вносим изменения в информацию о пользователе методом PUT

        url_put = base_url + resource + username
        print(url_put)

        put_body = {
            "id": 8,
            "username": change_username,
            "firstName": "Petr",
            "lastName": "Petrov",
            "email": "testingfor@gmail.com",
            "password": "4321",
            "phone": "88008008008",
            "userStatus": 0
        }

        response_put = Http_methods.put(url_put, put_body)
        print(response_put.text)
        return response_put

    @staticmethod
    def info_about_change_user():    # Запрашиваем информацию об измененном пользователе методом GET

        url_get = base_url + resource + change_username
        print(url_get)
        response_get = Http_methods.get(url_get)
        print(response_get.text)
        return response_get

    @staticmethod
    def delete_user():    # Удаляем пользователя методом DELETE

        url_delete = base_url + resource + change_username
        print(url_delete)
        response_delete = Http_methods.delete(url_delete)
        print(response_delete.text)
        return response_delete
