from setting.enums import RequestType, RestMethod, ResponseCode
from schemas.valid_schemas import valid_list_users, valid_user, valid_empty, valid_element, valid_list_elements, \
    valid_create_user, valid_put_path_user, valid_register_user, valid_login_ok, valid_register_login_error

users = [(RequestType.LIST_USERS, RestMethod.GET_METHOD, ResponseCode.OK, valid_list_users),
         (RequestType.SINGLE_USER, RestMethod.GET_METHOD, ResponseCode.OK, valid_user),
         (RequestType.USER_NOT_FOUND, RestMethod.GET_METHOD, ResponseCode.NOT_FOUND, valid_empty),
         (RequestType.LIST_RESOURCE, RestMethod.GET_METHOD, ResponseCode.OK, valid_list_elements),
         (RequestType.SINGLE_RESOURCE, RestMethod.GET_METHOD, ResponseCode.OK, valid_element),
         (RequestType.LIST_RESOURCE_NOT_FOUND, RestMethod.GET_METHOD, ResponseCode.NOT_FOUND, valid_empty),
         (RequestType.DELAYED_RESPONSE, RestMethod.GET_METHOD, ResponseCode.OK, valid_list_users)]
users_ids = ['Get list users', 'Get user', 'User not found', 'Get list resource',
             'Get single resource', 'Resource not found', 'Get list users with delayed']

new_users = [(RequestType.CREATE_USER, RestMethod.POST_METHOD, ResponseCode.CREATE, valid_create_user),
             (RequestType.SINGLE_USER, RestMethod.PUT_METHOD, ResponseCode.OK, valid_put_path_user),
             (RequestType.SINGLE_USER, RestMethod.PATCH_METHOD, ResponseCode.OK, valid_put_path_user),
             (RequestType.SINGLE_USER, RestMethod.DELETE_METHOD, ResponseCode.NO_CONTENT, valid_empty)]
new_users_ids = ['Create new user successful', 'Update user with PUT', 'Update user with PATCH', 'Delete user']

login_register_user = [(RequestType.REGISTER_USER, RestMethod.POST_METHOD, ResponseCode.OK, valid_register_user),
                       (RequestType.LOGIN_USER, RestMethod.POST_METHOD, ResponseCode.OK, valid_login_ok)]
login_register_user_ids = ['Register user successful', 'Login user successful']

login_register_user_error = [
    (RequestType.REGISTER_USER, RestMethod.POST_METHOD, ResponseCode.BAD_REQUEST, valid_register_login_error),
    (RequestType.LOGIN_USER, RestMethod.POST_METHOD, ResponseCode.BAD_REQUEST, valid_register_login_error)]
login_register_user_error_ids = ['Register user unsuccessful', 'Login user unsuccessful']

users_ui = [(RequestType.LIST_USERS, RestMethod.GET_METHOD),
            (RequestType.SINGLE_USER, RestMethod.GET_METHOD),
            (RequestType.USER_NOT_FOUND, RestMethod.GET_METHOD),
            (RequestType.LIST_RESOURCE, RestMethod.GET_METHOD),
            (RequestType.SINGLE_RESOURCE, RestMethod.GET_METHOD),
            (RequestType.LIST_RESOURCE_NOT_FOUND, RestMethod.GET_METHOD),
            (RequestType.DELAYED_RESPONSE, RestMethod.GET_METHOD)]
users_ui_ids = ['Get list users', 'Get user', 'User not found', 'Get list resource',
                'Get single resource', 'Resource not found', 'Get list users with delayed']

new_users_ui = [(RequestType.CREATE_USER, RestMethod.POST_METHOD),
                (RequestType.SINGLE_USER, RestMethod.PUT_METHOD),
                (RequestType.SINGLE_USER, RestMethod.PATCH_METHOD),
                (RequestType.SINGLE_USER, RestMethod.DELETE_METHOD)]
new_users_ui_ids = ['Create new user successful', 'Update user with PUT', 'Update user with PATCH', 'Delete user']

login_register_user_ui = [(RequestType.REGISTER_USER, RestMethod.POST_METHOD),
                          (RequestType.LOGIN_USER, RestMethod.POST_METHOD)]
login_register_user_ui_ids = ['Register user', 'Login user']
