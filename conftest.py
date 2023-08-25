import pytest
from selenium import webdriver

from register.models import LoginRegisterUserSuccess, CreateUpdateUser


@pytest.fixture(scope="session")
def create_user():
    return CreateUpdateUser.random_user()


@pytest.fixture(scope="session")
def register_login_users():
    return {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }


@pytest.fixture(scope="session")
def register_login_users_error():
    return {
            "email": "eve.holt@reqres.in",
        }


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()