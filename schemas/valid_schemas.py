valid_list_users = {
    "type": "object",
    "properties":
        {
            "page": {"type": "integer"},
            "per_page": {"type": "integer"},
            "total": {"type": "integer"},
            "total_page": {"type": "integer"},
            "data": {
                "type": "array",
                "items": [
                    {
                        "properties":
                            {
                                "id": {"type": "integer"},
                                "email": {"type ": "string"},
                                "first_name": {"type": "string"},
                                "last_name": {"type": "string"},
                                "avatar": {"type": "string"}
                            },
                        "required": ["id", "email", "first_name", "last_name", "avatar"]
                    }
                ]
            },
            "support": {
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                    "text": {"type": "string"}
                },
                "required": ["url", "text"]
            }
        },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"]
}

valid_user = {
    "type": "object",
    "properties":
        {
            "data":
                {
                    "type": "object",
                    "properties":
                        {
                            "id": {"type": "integer"},
                            "email": {"type": "string"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "avatar": {"type": "string"}
                        },
                    "required": ["id", "email", "first_name", "last_name", "avatar"]
                },
            "support":
                {
                    "type": "object",
                    "properties":
                        {
                            "url": {"type": "string"},
                            "text": {"type": "string"}
                        },
                    "required": ["url", "text"]
                }
        },
    "required": ["data", "support"]
}

valid_list_elements = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_page": {"type": "integer"},
        "data": {
            "type": "array",
            "items": [
                {
                    "properties":
                        {
                            "id": {"type": "integer"},
                            "name": {"type ": "string"},
                            "year": {"type": "integer"},
                            "color": {"type": "string"},
                            "pantone_value": {"type": "string"}
                        },
                    "required": ["id", "name", "year", "color", "pantone_value"]
                }
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"]
}

valid_element = {
    "type": "object",
    "properties":
        {
            "data":
                {
                    "type": "object",
                    "properties":
                        {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                            "year": {"type": "integer"},
                            "color": {"type": "string"},
                            "pantone_value": {"type": "string"}
                        },
                    "required": ["id", "name", "year", "color", "pantone_value"]
                },
            "support":
                {
                    "type": "object",
                    "properties":
                        {
                            "url": {"type": "string"},
                            "text": {"type": "string"}
                        },
                    "required": ["url", "text"]
                }
        },
    "required": ["data", "support"]
}

valid_create_user = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

valid_put_path_user = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["name", "job", "updatedAt"]
}

valid_register_user = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"},
    },
    "required": ["id", "token"]
}

valid_login_ok = {
    "type": "object",
    "properties": {
        "token": {"type": "string"},
    },
    "required": ["token"]
}

valid_register_login_error = {
    "type": "object",
    "properties": {
        "error": {"type": "string"}
    },
    "required": ["error"]
}

valid_empty = {}
