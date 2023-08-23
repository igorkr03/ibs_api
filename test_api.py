import allure
import jsonschema
import pytest

from parameters import users, users_ids, new_users, new_users_ids
from register.api import Register
from schemas.registration import valid_list_users

URL = "https://reqres.in/"


class TestAPI:

    def test_get_list_users(self):
        response = Register(url=URL).get_data(method='GET',
                                              url_api='api/users?page=2',
                                              schema=valid_list_users)
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=valid_list_users, response=response.response), \
                "Схема ответа не соотвествует заданной"

    @allure.parent_suite("AAAAAAAAAAA")
    # @allure.sub_suite("BBBBBBBBB")
    # @allure.story("SSSSSSSSSSSSSS")
    @allure.description("Проверяем API регистрации пользователя")
    @pytest.mark.parametrize('users_action', users, ids=users_ids)
    def test_create_update_delete_user(self, users_action, create_user):
        allure.dynamic.description(f"Проверка API '{users_action[0].value}'")
        body = create_user
        response = Register(url=URL).register_user(body=body,
                                                   method=users_action[1].value,
                                                   url_api=users_action[0].value)
        with allure.step(f"Проверяем что статус response '{users_action[2].value}'"):
            assert response.status == users_action[2].value

    @allure.parent_suite("AAAAAAAAAAA")
    # @allure.sub_suite("BBBBBBBBB")
    # @allure.story("SSSSSSSSSSSSSS")
    @allure.description("Проверяем API регистрации пользователя")
    @pytest.mark.parametrize('users_action', new_users, ids=new_users_ids)
    def register_login_user(self, users_action, register_login_users):
        allure.dynamic.description(f"Проверка API '{users_action[0].value}'")
        body = register_login_users
        response = Register(url=URL).register_user(body=body,
                                                   method=users_action[1].value,
                                                   url_api=users_action[0].value)
        with allure.step(f"Проверяем что статус response '{users_action[2].value}'"):
            assert response.status == users_action[2].value


def check_schema(schema, response):
    try:
        jsonschema.validate(instance=response, schema=schema)
        print("YESYES")
        return True
    except jsonschema.exceptions.ValidationError as ve:
        print("DFDFDFDDG", ve)
        return False
