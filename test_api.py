from time import sleep

import allure
import jsonschema
import pytest

from api_page import ApiPage
from enums import UrlResource as UR

from parameters import users, users_ids, new_users, new_users_ids, login_register_user, login_register_user_ids, \
    login_register_user_error, login_register_user_error_ids
from register.api import Register


class TestAPI:

    @pytest.mark.parametrize('users_action', users, ids=users_ids)
    def test_get_list_users(self, users_action):
        allure.dynamic.description(f"Проверка API {users_action[0].name} '{users_action[0].value}'")
        response = Register(url=UR.URL_REQRES.value).get_data(method=users_action[1].value,
                                                        url_api=users_action[0].value
                                                        )
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.parent_suite("AAAAAAAAAAA")
    # @allure.sub_suite("BBBBBBBBB")
    # @allure.story("SSSSSSSSSSSSSS")
    @allure.description("Проверяем API создания пользователя")
    @pytest.mark.parametrize('users_action', new_users, ids=new_users_ids)
    def test_create_update_delete_user(self, users_action, create_user):
        allure.dynamic.description(f"Проверка API {users_action[1].name} '{users_action[0].value}'")
        body = create_user
        response = Register(url=UR.URL_REQRES.value).action_user(body=body,
                                                                 method=users_action[1].value,
                                                                 url_api=users_action[0].value)
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.parent_suite("AAAAAAAAAAA")
    # @allure.sub_suite("BBBBBBBBB")
    # @allure.story("SSSSSSSSSSSSSS")
    @allure.description("Проверяем API при регистрации и логине пользователя")
    @pytest.mark.parametrize('users_action', login_register_user, ids=login_register_user_ids)
    def test_register_login_user(self, users_action, register_login_users):
        allure.dynamic.description(f"Проверка API {users_action[1].name} '{users_action[0].value}'")
        body = register_login_users
        response = Register(url=UR.URL_REQRES.value).action_user(body=body,
                                                                 method=users_action[1].value,
                                                                 url_api=users_action[0].value)
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.parent_suite("AAAAAAAAAAA")
    # @allure.sub_suite("BBBBBBBBB")
    # @allure.story("SSSSSSSSSSSSSS")
    @allure.description("Проверяем API при регистрации и логине пользователя с пропущенными полями")
    @pytest.mark.parametrize('users_action', login_register_user_error, ids=login_register_user_error_ids)
    def test_register_login_user_error(self, users_action, register_login_users_error):
        allure.dynamic.description(f"Проверка API {users_action[1].name} '{users_action[0].value}'")
        body = register_login_users_error
        response = Register(url=UR.URL_REQRES.value).action_user(body=body,
                                                                 method=users_action[1].value,
                                                                 url_api=users_action[0].value)
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.parent_suite("CCCCCCCCCCCC")
    # @allure.sub_suite("BBBBBBBBB")
    # @allure.story("SSSSSSSSSSSSSS")
    @allure.description("Проверяем коды ответа на странице")
    @pytest.mark.parametrize('users_action', login_register_user_error, ids=login_register_user_error_ids)
    def test_register_login_user_error_ui(self, browser, users_action, register_login_users_error):
        api_logics = ApiPage(browser)
        sleep(10)
        api_logics.go_to_site()
        sleep(10)
        allure.dynamic.description(f"Проверка кода ответа на API {users_action[1].name} '{users_action[0].value}'")
        body = register_login_users_error
        response = Register(url=UR.URL_REQRES.value).action_user(body=body,
                                                                 method=users_action[1].value,
                                                                 url_api=users_action[0].value)
        api_logics.click_api(name_api=users_action[0])
        with (allure.step(
                f'Проверяем что код ответа на странице соответствует коду ответа API "{users_action[2].value}"')):
            assert api_logics.check_response_code(name_api=users_action[0].value,
                                                  response_api=response), \
                'Код на странице не соответствует коду из API'


def check_schema(schema, response):
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
