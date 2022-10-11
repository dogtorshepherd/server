import json

from V1.services.majorService import MajorService
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("MajorController")


class MajorController:
    def getMajor(self):
        try:
            data = MajorService().getMajor()
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("MajorController getMajor Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)