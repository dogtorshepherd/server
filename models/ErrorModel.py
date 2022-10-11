from constants import httpError


class SystemErrorModel(Exception):
    def __init__(self,code,message,stack=None):
        super().__init__(code,message,stack)
        self.statusCode = code
        self.message = message
        self.httpCode = httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,
        self.stack = stack

class ClientErrorModel(Exception):
    def __init__(self, code, message,stack=None):
        self.statusCode = code
        self.message = message
        self.httpCode = httpError.HTTP_CLIENT_ERROR_HTTP_CODE
        self.stack = stack
