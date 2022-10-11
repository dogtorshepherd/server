from flask import Blueprint, request, jsonify

from constants import http, httpError
from eventRouters.teacherEventRouter import TeacherEventRouter
from eventRouters.userEventRouter import UserEventRouter
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from models.ResponseBasic import ResponseError
from modules.logger import Logger

logger = Logger().getLogger("TeacherRouter")
teacher_api = Blueprint('teacher', __name__)


@teacher_api.route("/teachers", methods=['GET'])
def teacher():
    try:
        version = request.headers.get("x-api-version")
        params = request.args.to_dict()
        if len(params) > 0:
            result = {
                '1.0.0': TeacherEventRouter().getTeachers(params)
            }[version]
        else:
            result = {
                '1.0.0': TeacherEventRouter().getTeachers({})
            }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("TeacherRouter teacher() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), httpError.HTTP_UN_AUTHORIZATION_HTTP_CODE
    except Exception as e:
        logger.error("TeacherRouter teacher() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode, e.message,e.stack)
        return jsonify(ResponseError(error) .__dict__), error.statusCode
