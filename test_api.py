import allure
import jsonschema
import pytest

from page_action.api_page import ApiPage
from setting.enums import UrlResource as UR
from setting.parameters import login_register_user_ui
from setting.parameters import login_register_user_ui_ids
from setting.parameters import new_users_ui
from setting.parameters import new_users_ui_ids

from setting.parameters import users, users_ids, new_users, new_users_ids, login_register_user, login_register_user_ids, \
    login_register_user_error, login_register_user_error_ids
from setting.parameters import users_ui
from setting.parameters import users_ui_ids
from api_base.api import ApiRequest


class TestAPI:

    @allure.suite('Проверка API')
    @allure.sub_suite("Проверка API запросов GET")
    @pytest.mark.parametrize('users_action', users, ids=users_ids)
    def test_get_list_users(self, users_action):
        allure.dynamic.title(f"Проверка API {users_action[0].name} '{users_action[0].value}'")
        response = ApiRequest(url=UR.URL_REQRES.value).get_data(method=users_action[1].value,
                                                                url_api=users_action[0].value
                                                                )
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.suite("Проверка API")
    @allure.sub_suite("Проверяем API создания пользователя")
    @pytest.mark.parametrize('users_action', new_users, ids=new_users_ids)
    def test_create_update_delete_user(self, users_action, create_user):
        allure.dynamic.title(f"Проверка API {users_action[1].name} '{users_action[0].value}'")
        body = create_user
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.suite("Проверка API")
    @allure.sub_suite("Проверяем API при регистрации и логине пользователя")
    @pytest.mark.parametrize('users_action', login_register_user, ids=login_register_user_ids)
    def test_register_login_user(self, users_action, register_login_users):
        allure.dynamic.title(f"Проверка API {users_action[1].name} '{users_action[0].value}'")
        body = register_login_users
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.suite("Проверка API")
    @allure.sub_suite("Проверяем API при регистрации и логине пользователя с пропущенными полями")
    @pytest.mark.parametrize('users_action', login_register_user_error, ids=login_register_user_error_ids)
    def test_register_login_user_error(self, users_action, register_login_users_error):
        allure.dynamic.title(f"Проверка API {users_action[1].name} '{users_action[0].value}'")
        body = register_login_users_error
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)
        with allure.step(f'Проверяем что код ответа "{users_action[2].value}"'):
            assert response.status == users_action[2].value
        with allure.step('Проверяем схему ответа'):
            assert check_schema(schema=users_action[3], response=response.response), \
                "Схема ответа не соответствует заданной"

    @allure.suite("Проверка UI ответов API")
    @allure.sub_suite("Проверяем коды ответа при GET запросах")
    @pytest.mark.parametrize('users_action', users_ui, ids=users_ui_ids)
    def test_get_list_users_ui(self, browser, users_action, register_login_users_error):
        allure.dynamic.title(f"Проверка API {users_action[0].name} '{users_action[0].value}'")
        api_logics = ApiPage(browser)
        api_logics.go_to_site()
        allure.dynamic.description(f"Проверка кода ответа на API {users_action[1].name} '{users_action[0].value}'")
        body = register_login_users_error
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)
        api_logics.click_api(name_method=users_action[0].name, type_method=users_action[1].value)
        with allure.step(
                f'Проверяем что код ответа на странице соответствует коду ответа API "{users_action[0].value}"'):
            assert api_logics.check_response_code(name_api=users_action[0].value,
                                                  response_api=response), \
                'Код на странице не соответствует коду из API'

    @allure.suite("Проверка UI ответов API")
    @allure.sub_suite("Проверяем коды ответа при создании нового пользователя")
    @pytest.mark.parametrize('users_action', new_users_ui, ids=new_users_ui_ids)
    def test_create_update_delete_user_ui(self, browser, users_action, register_login_users_error):
        allure.dynamic.title(f"Проверка API {users_action[0].name} '{users_action[0].value}'")
        api_logics = ApiPage(browser)
        api_logics.go_to_site()
        body = register_login_users_error
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)

        api_logics.click_api(name_method=users_action[0].name, type_method=users_action[1].value)
        with allure.step(
                f'Проверяем что код ответа на странице соответствует коду ответа API "{users_action[0].value}"'):
            assert api_logics.check_response_code(name_api=users_action[0].value,
                                                  response_api=response), \
                'Код на странице не соответствует коду из API'

    @allure.suite("Проверка UI ответов API")
    @allure.sub_suite("Проверяем коды ответа при регистрации и логине пользователя")
    @pytest.mark.parametrize('users_action', login_register_user_ui, ids=login_register_user_ui_ids)
    def test_register_login_user_ui(self, browser, users_action, register_login_users):
        allure.dynamic.title(f"Проверка API {users_action[0].name} '{users_action[0].value}'")
        api_logics = ApiPage(browser)
        api_logics.go_to_site()
        body = register_login_users
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)

        api_logics.click_api(name_method=users_action[0].name, type_method=users_action[1].value)
        with allure.step(
                f'Проверяем что код ответа на странице соответствует коду ответа API "{users_action[0].value}"'):
            assert api_logics.check_response_code(name_api=users_action[0].value,
                                                  response_api=response), \
                'Код на странице не соответствует коду из API'

    @allure.suite("Проверка UI ответов API")
    @allure.sub_suite("Проверяем коды ответа при неверной регистрации и логине пользователя")
    @pytest.mark.parametrize('users_action', login_register_user_ui, ids=login_register_user_ui_ids)
    def test_error_register_login_user_ui(self, browser, users_action, register_login_users_error):
        allure.dynamic.title(f"Проверка API {users_action[0].name} '{users_action[0].value}'")
        api_logics = ApiPage(browser)
        api_logics.go_to_site()
        body = register_login_users_error
        response = ApiRequest(url=UR.URL_REQRES.value).action_user(body=body,
                                                                   method=users_action[1].value,
                                                                   url_api=users_action[0].value)
        name_method = 'ERROR_' + users_action[0].name
        api_logics.click_api(name_method=name_method, type_method=users_action[1].value)
        with allure.step(
                f'Проверяем что код ответа на странице соответствует коду ответа API "{users_action[0].value}"'):
            assert api_logics.check_response_code(name_api=users_action[0].value,
                                                  response_api=response), \
                'Код на странице не соответствует коду из API'


def check_schema(schema, response):
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
