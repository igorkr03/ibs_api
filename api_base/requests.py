import requests


class Client:
    @staticmethod
    def custom_request(method: str, url: str, **kwargs):
        return requests.request(method, url, **kwargs)