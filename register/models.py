from ast import literal_eval
import random

from faker import Faker

fake = Faker()
list_jobs = ['leader', 'student', 'worker', 'administrator']


class CreateUpdateUser:
    @staticmethod
    def random_user():
        name = fake.name()
        job = random.choice(list_jobs)
        return {"name": name, "job": job}


class LoginRegisterUserSuccess:
    @staticmethod
    def random_user():
        email = fake.email()
        password = fake.password()
        return {"name": email, "password": password}


class LoginRegisterUserError:
    @staticmethod
    def random_user():
        email = fake.email()
        return {"name": email}


class ResponseModel:
    def __init__(self, status: int, response):
        self.status = status
        self.response = response
