from jsonschema import validate, exceptions

from register.models import ResponseModel
from register.requests import Client

class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    def register_user(self, body: dict, method: str, url_api: str):
        response = self.client.custom_request(method, f"{self.url}{url_api}", json=body)
        return ResponseModel(status=response.status_code, response=response.reason)

    def get_data(self, method: str, url_api: str, schema):
        response = self.client.custom_request(method, f"{self.url}{url_api}")
       # try:
       #     validate(instance=response.json(), schema=schema)
       #     print("YESYES")
       #except exceptions.ValidationError as ve:
       #     print("DFDFDFDDG", ve)
        #validate(instance=response.json(), schema=schema), "ERRROR"
        return ResponseModel(status=response.status_code, response=response.json())
