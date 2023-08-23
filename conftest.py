import pytest

from register.models import LoginRegisterUserSuccess, CreateUpdateUser


@pytest.fixture(scope="session")
def create_user():
    return CreateUpdateUser.random_user()


@pytest.fixture(scope="session")
def register_login_user():
    return LoginRegisterUserSuccess.random_user()
