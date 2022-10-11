import json

from V1.repositories.majorRepository import MajorRepository
from V1.utils.transformUtils import TransformUtils
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

logger = Logger().getLogger("MajorService")


class MajorService:

    def getMajor(self):
        try:
            majorRepo = MajorRepository()
            result = majorRepo.getMajor()
            resultList = []
            for item in result:
                logger.info(item)
                prenameModel = TransformUtils().toMajorModel(item['major_id'], item['major_name'])
                resultList.append(prenameModel)

            return resultList
        except Exception as e:
            logger.error("MajorService getMajor() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)