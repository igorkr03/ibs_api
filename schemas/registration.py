import ast

valid_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "uuid": {"type": "string"},
    },
    "required": ["message", "uuid"]
}

# valid_list_users = {
#     "page": "int",
#     "per_page": "int",
#     "total": "int",
#     "total_page": "int",
#     "data": [{
#         "id": "int",
#         "email": "string",
#         "first_name": "string",
#         "last_name": "string",
#         "avatar": "string"},
#     ],
#     "support": {"url": "string",
#                 "text": "string"}
# }

valid_list_users = {
  "type": "object",
  "properties": {
    "page": {
      "type": "integer"
    },
    "per_page": {
      "type": "integer"
    },
    "total": {
      "type": "integer"
    },
    "total_page": {
      "type": "integer"
    },
    "data": {
      "type": "array",
      "items": {
        "id": "integer",
        "email": "string",
        "first_name": "string",
        "last_name": "string",
        "avatar": "string"
      },
      "required": [
        "id",
        "email",
        "first_name",
        "last_name",
        "avatar"
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": ["page", "per_page", "total", "total_pages", "data", "support"]
}

valid_user = {
    "type": "object",
    "data": {"type": "array",
             "items": {
                 "id": "integer",
                 "email": "string",
                 "first_name": "string",
                 "last_name": "string",
                 "avatar": "string"},
             "required": ["id", "email", "first_name", "last_name", "avatar"]
             },
    "support": {"type": "object",
                "properties": {
                    "url": "string",
                    "text": "string"},
                "required": ["url", "text"]
                },
    "required": ["data", "support"]
}


def check_response(content):
    d = ast.literal_eval(content.decode)


schema = {
    "type": "object",
    "properties": {
        "employee": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer", "minimum": 0},
                "address": {
                    "type": "object",
                    "properties": {
                        "street": {
                            "type": "string"
                        },
                        "city": {
                            "type": "string"
                        },
                        "state": {
                            "type": "string"
                        },
                        "zip": {
                            "type": "string"
                        }
                    },
                    "required": ["street", "city", "state", "zip"]
                }
            },
            "required": ["name", "age", "address"]
        }
    },
    "required": ["employee"]
}
