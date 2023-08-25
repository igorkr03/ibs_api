import allure
from base_action import BasePage
from enums import RequestType
from locators import ApiPage as AP
from register.api import Register


class ApiPage(BasePage):

    def get_request(self):
        return self.get_text_element(locator=AP.FIELD_REQUEST)

    def get_response_code(self):
        return self.get_text_element(locator=AP.FIELD_RESPONSE_CODE)

    # def get_response_code(self, locator):
    #    return self.get_text_element(locator=locator)

    def click_api(self, name_api: RequestType):
        locator = get_locators(name_api=name_api)
        with allure.step(f'Проверяем что API "{name_api.name}" отображается на странице'):
            self.check_element(locator=locator)
        with allure.step(f'Нажимаем на API "{name_api.name}"'):
            self.click_element(locator=locator)

    def check_response_code(self, name_api: RequestType, response_api):
        response_ui = self.get_request()
        code_ui = self.get_response_code()
        # code_api = Register(url=url).action_user(body=body,
        #                                          method=users_action[1].value,
        #                                          url_api=users_action[0].value)
        return code_ui == response_api and response_ui == response_api


def get_locators(name_api):
    locator_api = {RequestType.GET_LIST_USERS: AP.LIST_USERS,
                   RequestType.GET_SINGLE_USER: AP.SINGLE_USER,
                   RequestType.GET_USER_NOT_FOUND: AP.SINGLE_USER_NOT_FOUND,
                   RequestType.GET_LIST_RESOURCE: AP.LIST_RESOURCE,
                   RequestType.GET_SINGLE_RESOURCE: AP.SINGLE_RESOURCE,
                   RequestType.GET_LIST_RESOURCE_NOT_FOUND: AP.SINGLE_RESOURCE_NOT_FOUND,
                   RequestType.CREATE_USER: AP.CREATE,
                   RequestType.UPDATE_USER: AP.UPDATE_PUT,
                   RequestType.REGISTER_USER: AP.REGISTER_SUCCESSFUL,
                   RequestType.LOGIN_USER: AP.LOGIN_SUCCESSFUL,
                   RequestType.DELAYED_RESPONSE: AP.DELAY}[name_api]
    return locator_api
