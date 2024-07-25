

class ClientError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message 


class ResourceNotFoundError(ClientError):
    def __init__(self, id):
        super().__init__(f"{id} not found")
        self.id = id

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message