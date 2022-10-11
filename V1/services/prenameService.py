import json

from V1.models.prenameModel import PrenameModel
from V1.queries import userQuery
from V1.repositories.prenameRepository import PrenameRepository
from V1.repositories.userRepository import UserRepository
from V1.utils.transformUtils import TransformUtils
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("PrenameService")


class PrenameService:

    def getPrenames(self):
        try:
            prenameRepo = PrenameRepository()
            result = prenameRepo.getPrename()
            resultList = []
            logger.info("result : " + str(result))
            logger.info("resultList : " + str(resultList))
            for item in result:
                logger.info(item)
                prenameModel = TransformUtils().toPrenameModel(item['prename_id'], item['prename_text'])
                resultList.append(prenameModel)

            return resultList
        except Exception as e:
            logger.error("PrenameService getPrenames() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)