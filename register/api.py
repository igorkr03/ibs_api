from jsonschema import validate, exceptions

from register.models import ResponseModel
from register.requests import Client

class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    def action_user(self, body: dict, method: str, url_api: str):
        response = self.client.custom_request(method, f"{self.url}{url_api}", json=body)
        response_data = {}
        if response.status_code != 204:
            response_data = response.json()
        return ResponseModel(status=response.status_code, response=response_data)

    def get_data(self, method: str, url_api: str):
        response = self.client.custom_request(method, f"{self.url}{url_api}")
        return ResponseModel(status=response.status_code, response=response.json())
