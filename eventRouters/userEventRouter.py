from V1.controllers.userController import UserController
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("UserEventRouter")


class UserEventRouter:
    def getAllUsers(self, params):
        try:
            result = UserController().getUsers(params)
            return result
        except Exception as e:
            logger.error("UserEventRouter getAllUsers() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def userLogin(self, body):
        try:
            result = UserController().userLogin(body)
            return result
        except Exception as e:
            logger.error("UserEventRouter getAdmin() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createUser(self, body):
        try:
            result = UserController().createUser(body)
            return result
        except Exception as e:
            logger.error("UserEventRouter createUser() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def editUser(self, body):
        try:
            result = UserController().editUser(body)
            return result
        except Exception as e:
            logger.error("UserEventRouter editUser() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteUser(self, params):
        try:
            result = UserController().deleteUser(params)
            return result
        except Exception as e:
            logger.error("UserEventRouter deleteUser() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def test(self, body):
        try:
            result = UserController().test(body)
            return result
        except Exception as e:
            logger.error("UserEventRouter createUser() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
