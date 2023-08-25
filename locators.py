from selenium.webdriver.common.by import By


class ApiPage:
    LIST_USERS = (By.XPATH, '//ul//li[@data-id="users"]')
    SINGLE_USER = (By.XPATH, '//ul//li[@data-id="users-single"]')
    SINGLE_USER_NOT_FOUND = (By.XPATH, '//ul//li[@data-id="users-single-not-found"]')
    LIST_RESOURCE = (By.XPATH, '//ul//li[@data-id="unknown"]')
    SINGLE_RESOURCE = (By.XPATH, '//ul//li[@data-id="unknown-single"]')
    SINGLE_RESOURCE_NOT_FOUND = (By.XPATH, '//ul//li[@data-id="unknown-single-not-found"]')
    CREATE = (By.XPATH, '//ul//li[@data-id="post"]')
    UPDATE_PUT = (By.XPATH, '//ul//li[@data-id="put"]')
    UPDATE_PATCH = (By.XPATH, '//ul//li[@data-id="patch"]')
    DELETE = (By.XPATH, '//ul//li[@data-id="DELETE"]')
    REGISTER_SUCCESSFUL = (By.XPATH, '//ul//li[@data-id="register-successful"]')
    REGISTER_UNSUCCESSFUL= (By.XPATH, '//ul//li[@data-id="register-unsuccessful"]')
    LOGIN_SUCCESSFUL = (By.XPATH, '//ul//li[@data-id="login-successful"]')
    LOGIN_UNSUCCESSFUL = (By.XPATH, '//ul//li[@data-id="login-unsuccessful"]')
    DELAY = (By.XPATH, '//ul//li[@data-id="delay"]')
    FIELD_REQUEST = (By.XPATH, '//div[@class="request"]//span[@class="url"]')
    FIELD_RESPONSE_CODE = (By.XPATH, '//div[@class="response"]//span[@class="response-code"]')
