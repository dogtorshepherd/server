from flask import Blueprint, jsonify, request
import json
from constants import http, httpError
from eventRouters.adminEventRouter import AdminEventRouter
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from models.ResponseBasic import ResponseError
from modules.logger import Logger

logger = Logger().getLogger("AdminRouter")
admin_api = Blueprint('admin', __name__)


@admin_api.route("/admin", methods=['GET'])
def admin():
    try:
        version = request.headers.get("x-api-version")
        params = request.args.to_dict()
        if len(params) > 0:
            result = {
                '1.0.0': AdminEventRouter().getAdmin(params)
            }[version]
        else:
            result = {
                '1.0.0': AdminEventRouter().getAllAdmin()
            }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("AdminRouter admin() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), error.httpCode
    except Exception as e:
        logger.error("AdminRouter admin() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            return jsonify(ResponseError(error)),httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE
        error = SystemErrorModel(e.statusCode, e.message, e.stack)
        return jsonify(ResponseError(error).__dict__), e.httpCode
