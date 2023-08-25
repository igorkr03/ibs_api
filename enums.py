from enum import Enum


class UrlResource(Enum):
    URL_REQRES = 'https://reqres.in'

    def __repr__(self):
        return self.value


class RequestType(Enum):
    GET_LIST_USERS = '/api/users?page=2'
    GET_SINGLE_USER = '/api/users/2'
    GET_USER_NOT_FOUND = '/api/users/23'
    GET_LIST_RESOURCE = '/api/unknown'
    GET_SINGLE_RESOURCE = '/api/unknown/2'
    GET_LIST_RESOURCE_NOT_FOUND = '/api/unknown/23'
    CREATE_USER = '/api/users'
    UPDATE_USER = '/api/users/2'
    REGISTER_USER = '/api/register'
    LOGIN_USER = '/api/login'
    DELAYED_RESPONSE = '/api/users?delay=3'


class ResponseCode(Enum):
    OK = 200
    CREATE = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    NOT_FOUND = 404


class RestMethod(Enum):
    GET_METHOD = 'GET'
    POST_METHOD = 'POST'
    PUT_METHOD = 'PUT'
    PATCH_METHOD = 'PATCH'
    DELETE_METHOD = 'DELETE'

