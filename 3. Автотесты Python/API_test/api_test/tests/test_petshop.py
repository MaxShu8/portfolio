from requests import Response
from utils.api_petshop import Create_new_user
from utils.checking_1 import Checking


class Test_create_update_delete_user():

    def test_create_update_delete_user(self):

        print(f'\n -----создание нового пользователя (POST)')
        result_post: Response = Create_new_user.create_new_user()
        Checking.check_status_code(result_post, 200)

        print(f'\n -----запрос информации о новом пользователе (GET)')
        result_get: Response = Create_new_user.info_about_user()
        Checking.check_status_code(result_get, 200)

        print(f'\n -----изменение информации пользователя (PUT)')
        result_put: Response = Create_new_user.update_user()
        Checking.check_status_code(result_put, 200)

        print(f'\n -----запрос информации об измененном пользователе (GET)')
        result_get: Response = Create_new_user.info_about_change_user()
        Checking.check_status_code(result_get, 200)

        print(f'\n -----удаление пользователя (DELETE)')
        result_delete: Response = Create_new_user.delete_user()
        Checking.check_status_code(result_delete, 200)

        print(f'\n -----запрос информации об измененном пользователе (GET)')
        result_get: Response = Create_new_user.info_about_change_user()
        Checking.check_status_code(result_get, 404)

