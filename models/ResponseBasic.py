import math

from constants import http


class ResponseBasic:
    def __init__(self, code, message):
        self.statusCode = code
        self.message = message


class ResponseSuccessWithData:
    def __init__(self, data):
        self.statusCode = http.HTTP_SUCCESS_CODE
        self.message = http.HTTP_SUCCESS_MSG
        self.result = data

class ResponseSuccessWithDataPaginate:
    def __init__(self, data,pageNo,pageSize,totalRecord):
        self.statusCode = http.HTTP_SUCCESS_CODE
        self.message = http.HTTP_SUCCESS_MSG
        self.result = {
            'totalPage': math.ceil(totalRecord/pageSize),
            'totalRecord': totalRecord,
            'pageNo': pageNo,
            'pageSize': pageSize,
            'data': data
        }


class ResponseSuccess:
    def __init__(self):
        self.statusCode = http.HTTP_SUCCESS_CODE
        self.message = http.HTTP_SUCCESS_MSG

class ResponseError:
    def __init__(self,error):
        self.statusCode = error.statusCode
        self.statusMessage = error.message
        self.stack = error.stack