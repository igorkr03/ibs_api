import allure
from page_action.base_action import BasePage
from setting.enums import RequestType
from page_action.locators import ApiPage as AP


class ApiPage(BasePage):

    def get_request(self):
        return self.get_text_element(locator=AP.FIELD_REQUEST)

    def get_response_code(self):
        return self.get_text_element(locator=AP.FIELD_RESPONSE_CODE)

    def click_api(self, name_method, type_method):
        name_api = {'GET': name_method + '_' + type_method,
                    'POST': name_method + '_' + type_method,
                    'PUT': name_method + '_' + type_method,
                    'PATCH': name_method + '_' + type_method,
                    'DELETE': name_method + '_' + type_method}[type_method]
        locator = get_locators(name_api=name_api)
        with allure.step(f'Проверяем что API "{name_method}" отображается на странице'):
            self.check_element(locator=locator)
        with allure.step(f'Нажимаем на API "{name_method}"'):
            self.click_element(locator=locator)

    def check_response_code(self, name_api: RequestType, response_api):
        response_ui = self.get_request()
        code_ui = self.get_response_code()
        return code_ui == str(response_api.status) and response_ui == name_api


def get_locators(name_api):
    locator_api = {'LIST_USERS_GET': AP.LIST_USERS,
                   'SINGLE_USER_GET': AP.SINGLE_USER,
                   'USER_NOT_FOUND_GET': AP.SINGLE_USER_NOT_FOUND,
                   'LIST_RESOURCE_GET': AP.LIST_RESOURCE,
                   'SINGLE_RESOURCE_GET': AP.SINGLE_RESOURCE,
                   'LIST_RESOURCE_NOT_FOUND_GET': AP.SINGLE_RESOURCE_NOT_FOUND,
                   'CREATE_USER_POST': AP.CREATE,
                   'SINGLE_USER_PUT': AP.UPDATE_PUT,
                   'SINGLE_USER_PATCH': AP.UPDATE_PATCH,
                   'SINGLE_USER_DELETE': AP.DELETE,
                   'REGISTER_USER_POST': AP.REGISTER_SUCCESSFUL,
                   'LOGIN_USER_POST': AP.LOGIN_SUCCESSFUL,
                   'ERROR_REGISTER_USER_POST': AP.REGISTER_UNSUCCESSFUL,
                   'ERROR_LOGIN_USER_POST': AP.LOGIN_UNSUCCESSFUL,
                   'DELAYED_RESPONSE_GET': AP.DELAY}[name_api]
    return locator_api
