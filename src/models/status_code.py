from enum import Enum
#enum is like dictionary: a name and a value

class StatusCode(Enum):
    OK = 200
    BadRequest = 400
    Unautherized = 401
    NotFound = 404
    InternalServerError = 500