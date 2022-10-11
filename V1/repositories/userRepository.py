import json

from V1.queries import userQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger
import numpy as np

logger = Logger().getLogger("UserRepository")


class UserRepository:
    dbConnector = DBConnector("test")

    def getUsers(self,whereClause,params):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(userQuery.FIND_USERS(whereClause),params)

            return self.cursor.fetchall()
        except Exception as e:
            logger.error("UserRepository getUsers() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def userLogin(self, username, password):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            logger.info("QUERY : " + userQuery.USER_LOGIN(username, password))
            self.cursor.execute(userQuery.USER_LOGIN(username, password))
            result = {}
            item = self.cursor.fetchone()
            result["isUserExist"] = False
            result["isLoginSuccess"] = False
            if item :
                result["isUserExist"] = item["USER_EXIST"]
                result["isLoginSuccess"] = item["USER_LOGIN"]
                result["username"] = item["user_username"]
                result["userId"] = item["user_id"]
                result["userType"] = item["user_type"]
                result["firstname"] = item["user_firstname"]
                result["lastname"] = item["user_lastname"]
                result["email"] = item["user_email"]
                result["prenameId"] = item["user_prename"]
                result["prenameText"] = item["prename_text"]
            return str(result)
        except Exception as e:
            logger.error("UserRepository userLogin Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()


    def createUser(self, type, username, password, prename, firstname, lastname ):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()

            self.cursor.execute(userQuery.INSERT_USER,(username,password,prename,firstname,lastname,type,"test@test.test"))
            result = {}
            result["userId"] = self.cursor.lastrowid
            result["username"] = username
            return result

        except Exception as e:
            self.con.rollback()
            logger.error("UserRepository createUser Exception: " + json.dumps(e.__dict__))
            self.con.rollback()
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def editUser(self, type, prename, firstname, lastname, userId ):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()

            self.cursor.execute(userQuery.EDIT_USER,(prename,firstname,lastname,type, userId))
            result = {}
            result["userId"] = userId
            return result

        except Exception as e:
            self.con.rollback()
            logger.error("UserRepository editUser Exception: " + json.dumps(e.__dict__))
            self.con.rollback()
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def deleteUser(self,userId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(userQuery.DELETE_USER,(userId,))
            result = {}
            result["userId"] = userId
            return result

        except Exception as e:
            self.con.rollback()
            logger.error("UserRepository editUser Exception: " + json.dumps(e.__dict__))
            self.con.rollback()
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def testQuery(self):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            params = ()
            self.cursor.execute("INSERT INTO test.test_table (id) VALUES(2)")
            self.cursor.execute("SELECT * FROM test.test_table")
            testResult = self.cursor.fetchall()
            self.con.rollback()

            self.cursor.execute("INSERT INTO test.test_table (id) VALUES(2)")
            self.cursor.execute("SELECT * FROM test.test_table")
            expectResult = self.cursor.fetchall()

            return {"test": testResult, "expect": expectResult, "compare": np.array_equal(testResult,expectResult)}
        except Exception as e:
            logger.error("TEST testQuery() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            # self.con.commit()
            self.cursor.close()
            self.con.close()
