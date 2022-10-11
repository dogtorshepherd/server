import json

from V1.services.userService import UserService
from constants import httpError
from models.ErrorModel import SystemErrorModel, ClientErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("UserController")


class UserController:
    def getUsers(self, params):
        try:
            userId =""
            if 'userId' in params:
                userId = params['userId']
            data = UserService().getUsers(userId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("UserController userLogin Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def userLogin(self, body):
        try:
            if len(body) <= 0:
                raise ClientErrorModel(httpError.HTTP_CLIENT_ERROR_STATUS_CODE, httpError.HTTP_CLIENT_ERROR_MSG,
                                       {'code': httpError.HTTP_CLIENT_ERROR_STATUS_CODE,
                                        'msg': "payload ว่าง กรุณาใส่ข้อมูลให้ถูกต้อง"})
            if "username" not in body or "password" not in body:
                raise ClientErrorModel(httpError.HTTP_CLIENT_ERROR_STATUS_CODE, httpError.HTTP_CLIENT_ERROR_MSG,
                                       {'code': httpError.HTTP_CLIENT_ERROR_STATUS_CODE,
                                        'msg': "payload ว่าง กรุณาใส่ข้อมูลให้ถูกต้อง"})
            username = body['username']
            password = body['password']
            data = UserService().userLogin(username, password)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("UserController userLogin Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createUser(self, body):
        try:
            if len(body) <= 0:
                raise ClientErrorModel(httpError.HTTP_CLIENT_ERROR_STATUS_CODE, httpError.HTTP_CLIENT_ERROR_MSG,
                                       {'code': httpError.HTTP_CLIENT_ERROR_STATUS_CODE,
                                        'msg': "payload ว่าง กรุณาใส่ข้อมูลให้ถูกต้อง"})
            #check type
            if "username" not in body or "password" not in body:
                raise ClientErrorModel(httpError.HTTP_CLIENT_ERROR_STATUS_CODE, httpError.HTTP_CLIENT_ERROR_MSG,
                                       {'code': httpError.HTTP_CLIENT_ERROR_STATUS_CODE,
                                        'msg': "payload ว่าง กรุณาใส่ข้อมูลให้ถูกต้อง"})
            username = body['username']
            password = body['password']
            prename = body['prename']
            firstname = body['firstname']
            lastname = body['lastname']
            type = body['type']
            admin = body['admin']
            teacher = body['teacher']
            student = body['student']
            data = {}
            if type == "ADMIN":
                data = admin
            elif type == "TEACHER":
                data = teacher
            else:
                data = student
            data = UserService().createUser(type,username, password, prename, firstname,lastname,data)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("UserController createUser Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def editUser(self, body):
        try:
            if len(body) <= 0:
                raise ClientErrorModel(httpError.HTTP_CLIENT_ERROR_STATUS_CODE, httpError.HTTP_CLIENT_ERROR_MSG,
                                       {'code': httpError.HTTP_CLIENT_ERROR_STATUS_CODE,
                                        'msg': "payload ว่าง กรุณาใส่ข้อมูลให้ถูกต้อง"})
            if "user_id" not in body :
                raise ClientErrorModel(httpError.HTTP_CLIENT_ERROR_STATUS_CODE, httpError.HTTP_CLIENT_ERROR_MSG,
                                       {'code': httpError.HTTP_CLIENT_ERROR_STATUS_CODE,
                                        'msg': "payload ว่าง กรุณาใส่ข้อมูลให้ถูกต้อง"})

            userId = body['user_id']
            prename = body['prename']
            firstname = body['firstname']
            lastname = body['lastname']
            type = body['type']
            admin = body['admin']
            teacher = body['teacher']
            student = body['student']
            data = {}
            if type == "ADMIN":
                data = admin
            elif type == "TEACHER":
                data = teacher
            else:
                data = student
            data = UserService().editUser(userId, type, prename, firstname,lastname,data)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("UserController editUser Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteUser(self, params):
        try:
            userId =""
            if 'userId' in params:
                userId = params['userId']
            data = UserService().deleteUser(userId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("UserController deleteUser Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)


    def test(self, body):
        try:
            data = UserService().test()
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("UserController createUser Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
