from enums import RequestType, RestMethod, ResponseCode

users = [(RequestType.CREATE_USER, RestMethod.POST_METHOD, ResponseCode.CREATE),
         (RequestType.UPDATE_USER, RestMethod.PUT_METHOD, ResponseCode.OK),
         (RequestType.UPDATE_USER, RestMethod.PATCH_METHOD, ResponseCode.OK),
         (RequestType.UPDATE_USER, RestMethod.DELETE_METHOD, ResponseCode.NO_CONTENT)
         ]
users_ids = ['Create user', 'Put user', 'Patch user', 'Delete user']

new_users = [(RequestType.REGISTER_USER, RestMethod.POST_METHOD, ResponseCode.OK),
             #(RequestType.REGISTER_USER, RestMethod.POST_METHOD, ResponseCode.BAD_REQUEST),
             (RequestType.LOGIN_USER, RestMethod.POST_METHOD, ResponseCode.OK),
             #(RequestType.LOGIN_USER, RestMethod.POST_METHOD, ResponseCode.BAD_REQUEST)
             ]
new_users_ids = ['Register new user successful', #'Register new user unsuccessful',
                 'Login user successful'#, 'Login user unsuccessful'
                 ]
