from flask import Blueprint, jsonify, request
import json
from constants import http, httpError
from eventRouters.testEventRouter import TestEventRouter
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from models.ResponseBasic import ResponseError
from modules.logger import Logger
logger = Logger().getLogger("TestRouter")
test_api = Blueprint('test', __name__)


@test_api.route("/test", methods=['GET'])
def test():
    try:
        version = request.headers.get("x-api-version")
        result = {
            '1.0.0': TestEventRouter().testApi()
        }[version]

        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("TestRouter test() Exception : "+str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG)
        return jsonify(ResponseError(error).__dict__),error.httpCode
    except Exception as e:
        logger.error("TestRouter test() Exception : "+str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode,e.message,e.stack)
        return jsonify(ResponseError(error).__dict__), error.httpCode
