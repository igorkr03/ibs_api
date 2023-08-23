import datetime
import os
import pytest


if __name__ == '__main__':
    dir_allure = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    pytest.main(['test_api.py', '--alluredir', './report/allure_' + dir_allure])
    os.system('allure serve report/allure_' + dir_allure)
