import json

from V1.models.prenameModel import PrenameModel
from V1.queries import userQuery
from V1.repositories.courseRepository import CourseRepository
from V1.repositories.majorRepository import MajorRepository
from V1.repositories.prenameRepository import PrenameRepository
from V1.repositories.userRepository import UserRepository
from V1.utils.transformUtils import TransformUtils
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("CourseService")


class CourseService:

    def getCourse(self):
        try:
            courseRepo = CourseRepository()
            result = courseRepo.getAllCourse()
            resultList = []
            for item in result:
                logger.info(item)
                courseModel = TransformUtils().toCourseModel(item['course_id'], item['course_name'])
                resultList.append(courseModel)

            return resultList
        except Exception as e:
            logger.error("CourseService getCourse() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)