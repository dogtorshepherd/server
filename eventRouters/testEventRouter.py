from V1.controllers.TestController import TestController
from constants import http, httpError
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from modules.logger import Logger

logger = Logger().getLogger("TestEventRouter")


class TestEventRouter:
    def testApi(self):
        try:
            result = TestController().test()
            return result
        except Exception as e:
            logger.error("TestEventRouter testApi Exception : ")
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode,e.message)
