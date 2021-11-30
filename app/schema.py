

USER_CREATE = {
	"type": "object",
	"properties": {

		"email": {
			"type": "string",
			"pattern": """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
		},

		"password": {
			"type": "string",
			"pattern": "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
		}
	},
	"required": ["email", "password"]
}

ADVERTISEMENT_CREATE = {
    "type": "object",
    "properties": {

        "title": {
            "type": "string",
        },

        "owner": {
            "type": "integer",
        },
        "creation_date": {
            "type": "string",
            "pattern": r"^\d{4}-\d{2}-\d{2}$"
        }
    },
    "required": ["owner", "title"]
}

ADVERTISEMENT_PUT = {
    "type": "object",
    "properties": {

        "title": {
            "type": "string",
        },

        "owner_id": {
            "type": "integer",
        },
        "creation_date": {
            "type": "string",
            "pattern": r"^\d{4}-\d{2}-\d{2}$"
        }
    },
    "required": ["owner_id", "title"]
}

ADVERTISEMENT_PATCH = {
    "type": "object",
    "properties": {

        "title": {
            "type": "string",
        },

        "owner_id": {
            "type": "integer",
        },
        "creation_date": {
            "type": "string",
            "pattern": r"^\d{4}-\d{2}-\d{2}$"
        }
    }
}
