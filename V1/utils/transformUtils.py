from V1.models.courseModel import CourseModel
from V1.models.majorModel import MajorModel
from V1.models.prenameModel import PrenameModel
from V1.models.teacherModel import TeacherModel
from modules.logger import Logger

logger = Logger().getLogger("PrenameService")


class TransformUtils:
    def toPrenameModel(self,prenameId,prenameText):
        prenameModel = PrenameModel(prenameId, prenameText)
        logger.info(prenameModel.__dict__)
        return prenameModel.__dict__

    def toMajorModel(self,majorId,majorName):
        majorModel = MajorModel(majorId, majorName)
        logger.info(majorModel.__dict__)
        return majorModel.__dict__

    def toCourseModel(self,courseId, courseName):
        courseModel = CourseModel(courseId, courseName)
        logger.info(courseModel.__dict__)
        return courseModel.__dict__

    def toTeacherModel(self,userId,teacherId,teacherPhone,username,password,prenameId,prenameText,firstname,lastname,email,type):
        teacherModel = TeacherModel(userId,teacherId,teacherPhone,username,password,prenameId,prenameText,firstname,lastname,email,type);
        logger.info(teacherModel)
        return teacherModel.__dict__