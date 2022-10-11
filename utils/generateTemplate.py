import json
import random

from constants import httpError
from constants.queries import QUERY_RAND_DATA, QUERY_COUNT_DATA
from constants.template import TEMPLATES, OPTION_TEMPLATE, CLAUSES
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger
from utils.templateDecoder import TemplateDecoder

log = Logger()
logger = log.getLogger("GenerateTemplate")


class GenerateTemplate:
    dbConnector = DBConnector()

    # def generateSelectQuestion(self, cmd, skillType, database, table, dbObject):
    #     filedExtraList = ['UPPER', 'LOWER', 'AVG', 'MIN', 'MAX', 'COUNT', 'SUM', 'DISTINCT', 'FILED_NAME']
    #     oprRandList = ["=", ">", "<", "<>", ">=", "<=", "BETWEEN", "LIKE", "IN"]
    #     optionalList = ["WHERE", "GROUP BY", "ORDER BY"]
    #     try:
    #         self.con = self.dbConnector.connect()
    #         self.cusor = self.dbConnector.getCursor()
    #         self.data = TEMPLATES[cmd.upper()]
    #         self.template = ""
    #         listColumn = dbObject['columns']
    #
    #         filedNum = len(listColumn)
    #         self.template = self.data.replace("[remember|understand|implement|analysis]", skillType.upper())
    #
    #         if cmd.upper() == "SELECT":
    #             column = "<COLUMN>*|<OPTION><UPPER><FILED_NAME/>[<NAME/>]</UPPER>|<LOWER><FILED_NAME/>[<NAME/>]</LOWER>|<AVG><FILED_NAME/>[<NAME/>]</AVG>|<MIN><FILED_NAME/>[<NAME/>]</MIN>|<MAX><FILED_NAME/>[<NAME/>]</MAX>|<COUNT>*|<FILED_NAME/>[<NAME/>]</COUNT>|<SUM><FILED_NAME/>[<NAME/>]</SUM>|<FILED_NAME><VALUE/>[<NAME/>]</FILED_NAME>|<DISTINCT><FILED_NAME/>[<NAME/>]</DISTINCT></OPTION></COLUMN>"
    #             index = random.randint(0, 1)
    #             if index == 0:
    #                 self.template = self.template.replace(column, "<COLUMN>*</COLUMN>")
    #             else:
    #                 numFiled = random.randint(0, filedNum)
    #                 listFiled = []
    #                 colList = []
    #
    #                 # RAND FILED COLUMN OF TEMPLATE
    #                 i = numFiled
    #                 while i > 0:
    #                     print("LOOP")
    #                     iRand = random.randint(0, len(filedExtraList) - 1)
    #                     if filedExtraList[iRand] not in colList or filedExtraList[iRand] == "FILED_NAME":
    #                         colList.append(filedExtraList[iRand])
    #                         i -= 1
    #
    #                 i = numFiled
    #                 breakNum = i * 2
    #                 # Rand Filed IN DB
    #                 while i > 0 and breakNum > 0:
    #                     print("LOOP2")
    #                     print("COLUMN NAME == ", colList[numFiled - i])
    #                     iRand = random.randint(0, filedNum - 1)
    #                     if listColumn[iRand]['column_name'] not in listFiled:
    #                         if colList[numFiled - i] in listColumn[iRand]['column_comment']:
    #                             listFiled.append(listColumn[iRand]['column_name'])
    #                             i -= 1
    #                         elif colList[numFiled - i] in ["FILED_NAME", "DISTINCT"]:
    #                             listFiled.append(listColumn[iRand]['column_name'])
    #                             i -= 1
    #                         else:
    #                             while True:
    #                                 indexRand = random.randint(0, len(filedExtraList) - 1)
    #                                 if colList[numFiled - i] != filedExtraList[indexRand] and filedExtraList[
    #                                     indexRand] not in colList:
    #                                     colList[numFiled - i] = filedExtraList[indexRand]
    #                                     break
    #
    #                 new_column = ""
    #                 new_column += "<COLUMN><OPTION>"
    #                 for item in colList:
    #                     isName = False
    #                     if random.randint(0, 1) == 1:
    #                         isName = True
    #
    #                     if item == "FILED_NAME":
    #                         new_column += "<" + item + ">"
    #                         new_column += listFiled[colList.index(item)]
    #                         new_column += "</" + item + ">"
    #                     else:
    #                         new_column += "<" + item + ">"
    #                         new_column += "<FILED_NAME>" + listFiled[colList.index(item)] + "</FIELD_NAME>"
    #                         if isName:
    #                             new_column += "<NAME>" + listFiled[colList.index(item)].upper() + "</NAME>"
    #                         new_column += "</" + item + ">"
    #                 new_column += "</OPTION></COLUMN>"
    #
    #                 print("LIST FILED : ", listFiled)
    #                 print("LIST COL TEMP : ", colList)
    #
    #                 self.template = self.template.replace(column, new_column)
    #
    #             optional = "[<OPTION [SEQ]><WHERE><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/><OPERATOR>=|>|<|<>|>=|<=|LIKE|BETWEEN|IN</OPERATOR><VALUE/>[<VALUE2/>][<VALUES/>]</CON></WHERE>|(<GROUPBY><FILED_NAME/></GROUPBY>|<HAVING><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/>|[<AVG/>|<MIN/>|<MAX/>|<COUNT/>|<SUM/>]<OPERATOR>=|<|<>|>|>=|<=|LIKE|BETWEEN</OPERATOR><VALUE/>[<VALUE2/>]</CON><HAVING/>)|<ORDERBY><FILED_NAME/><VALUE>ASC|DESC</VALUE></ORDERBY></OPTION>]"
    #
    #             nOpional = []
    #             numOptional = random.randint(1, len(optionalList) - 1)
    #             i = numOptional
    #             while i > 0:
    #                 print("LOOP3")
    #                 randI = random.randint(0, len(optionalList) - 1)
    #                 if optionalList[randI] not in nOpional:
    #                     nOpional.append(optionalList[randI])
    #                     i -= 1
    #             new_option = ""
    #             if random.randint(0, 1) == 1:
    #                 new_option = "<OPTION>"
    #                 if "WHERE" in nOpional:
    #                     whereTemp = "<WHERE>"
    #                     numCon = random.randint(1, filedNum)
    #                     filedConList = []
    #                     filedConObjList = []
    #                     i = numCon
    #                     while i > 0:
    #                         print("LOOP5")
    #                         if listColumn[numCon - i]["column_name"] not in filedConList:
    #                             filedConList.append(listColumn[numCon - i]["column_name"])
    #                             filedConObjList.append(listColumn[numCon - i])
    #                             i -= 1
    #                     i = numCon
    #                     while i > 0:
    #                         print("LOOP6")
    #                         whereTemp += "<CON>"
    #                         if i != numCon:
    #                             whereTemp += "<PRE>"
    #                             if random.randint(0, 1) == 1:
    #                                 whereTemp += "AND"
    #                             else:
    #                                 whereTemp += "OR"
    #                             whereTemp += "</PRE>"
    #                         whereTemp += "<FILED_NAME>" + filedConList[numCon - i] + "</FILED_NAME>"
    #                         while True:
    #                             oprRandI = random.randint(0, 8)
    #                             # sql = "select COUNT(*) AS NUM from information_schema.columns " \
    #                             #       "where table_schema = %s and TABLE_NAME = %s and COLUMN_NAME = %s and COLUMN_COMMENT LIKE %s order by table_name,ordinal_position"
    #                             # queryParams = [database, table, filedConList[numCon - i],
    #                             #                '%' + oprRandList[oprRandI] + '%']
    #                             # cursor.execute(sql, queryParams)
    #                             # row = cursor.fetchone()
    #                             # if row['NUM'] > 0:
    #                             if oprRandList[oprRandI] in filedConObjList[numCon - i]['column_comment']:
    #                                 break
    #
    #                         whereTemp += "<OPERATOR>&" + oprRandList[oprRandI] + "&</OPERATOR>"
    #                         if oprRandI == 6:
    #                             sql = "SELECT " + filedConList[
    #                                 numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 2"
    #                             self.cursor.execute(sql)
    #                             word = []
    #                             for row in self.cursor.fetchall():
    #                                 word.append(row[filedConList[numCon - i]])
    #                             whereTemp += "<VALUE>" + str(min(word)) + "</VALUE><VALUE2>" + str(
    #                                 max(word)) + "</VALUE2>"
    #                         elif oprRandI == 7:
    #                             word = ""
    #                             if random.randint(0, 1) == 1:
    #                                 word += "%"
    #                             sql = "SELECT " + filedConList[
    #                                 numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 1"
    #                             self.cursor.execute(sql)
    #                             row = self.cursor.fetchone()
    #                             word += row[filedConList[numCon - i]]
    #                             if random.randint(0, 1) == 1:
    #                                 word += "%"
    #                             whereTemp += "<VALUE>" + str(word) + "</VALUE>"
    #                         elif oprRandI == 8:
    #                             num = random.randint(1, 8)
    #                             sql = "SELECT " + filedConList[
    #                                 numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT " + str(num)
    #                             self.cursor.execute(sql)
    #                             word = ""
    #                             for row in self.cursor.fetchall():
    #                                 word += "<VALUE>" + str(row[filedConList[numCon - i]]) + "</VALUE>"
    #                             whereTemp += "<VALUES>" + str(word) + "</VALUES>"
    #                         whereTemp += "</CON>"
    #                         i -= 1
    #                     whereTemp += "</WHERE>"
    #                     new_option += whereTemp
    #                 if "GROUP BY" in nOpional:
    #                     n = random.randint(1, filedNum)
    #                     filedGroupList = []
    #                     groupByTemp = "<GROUPBY>"
    #                     i = n
    #                     while i > 0:
    #                         print("LOOP7")
    #                         randI = random.randint(0, len(listColumn) - 1)
    #                         if listColumn[randI]["column_name"] not in filedGroupList:
    #                             filedGroupList.append(listColumn[randI])
    #                             groupByTemp += "<FILED_NAME>" + listColumn[randI]["column_name"] + "</FILED_NAME>"
    #                             i -= 1
    #                     groupByTemp += "</GROUPBY>"
    #                     new_option += groupByTemp
    #                     if random.randint(0, 1) == 1:
    #                         havingTemp = "<HAVING>"
    #                         whereTemp = ""
    #                         numCon = random.randint(1, filedNum)
    #                         filedConList = []
    #                         i = numCon
    #                         while i > 0:
    #                             print("LOOP8")
    #                             if listColumn[numCon - i]["column_name"] not in filedConList:
    #                                 filedConList.append(listColumn[numCon - i]["column_name"])
    #                                 i -= 1
    #                         i = numCon
    #                         while i > 0:
    #                             print("LOOP9")
    #                             whereTemp += "<CON>"
    #                             if i != numCon:
    #                                 whereTemp += "<PRE>"
    #                                 if random.randint(0, 1) == 1:
    #                                     whereTemp += "AND"
    #                                 else:
    #                                     whereTemp += "OR"
    #                                 whereTemp += "</PRE>"
    #                             whereTemp += "<FILED_NAME>" + filedConList[numCon - i] + "</FILED_NAME>"
    #                             opr = ""
    #                             oprRandI = -1
    #                             print("IIII2")
    #                             while True:
    #                                 oprRandI = random.randint(0, 8)
    #                                 sql = "select COUNT(*) AS NUM from information_schema.columns " \
    #                                       "where table_schema = %s and TABLE_NAME = %s and COLUMN_NAME = %s and COLUMN_COMMENT LIKE %s order by table_name,ordinal_position"
    #                                 queryParams = [database, table, filedConList[numCon - i],
    #                                                '%' + oprRandList[oprRandI] + '%']
    #                                 cursor.execute(sql, queryParams)
    #                                 row = cursor.fetchone()
    #                                 print("IIII")
    #                                 if row['NUM'] > 0:
    #                                     break
    #
    #                             whereTemp += "<OPERATOR>&" + oprRandList[oprRandI] + "&</OPERATOR>"
    #                             if oprRandI == 6:
    #                                 sql = "SELECT " + filedConList[
    #                                     numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 2"
    #                                 cursor.execute(sql)
    #                                 word = []
    #                                 for row in cursor.fetchall():
    #                                     word.append(row[filedConList[numCon - i]])
    #                                 whereTemp += "<VALUE>" + str(min(word)) + "</VALUE><VALUE2>" + str(
    #                                     max(word)) + "</VALUE2>"
    #                             elif oprRandI == 7:
    #                                 word = ""
    #                                 if random.randint(0, 1) == 1:
    #                                     word += "%"
    #                                 sql = "SELECT " + filedConList[
    #                                     numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 1"
    #                                 cursor.execute(sql)
    #                                 row = cursor.fetchone()
    #                                 word += row[filedConList[numCon - i]]
    #                                 if random.randint(0, 1) == 1:
    #                                     word += "%"
    #                                 whereTemp += "<VALUE>" + str(word) + "</VALUE>"
    #                             elif oprRandI == 8:
    #                                 num = random.randint(1, 8)
    #                                 sql = "SELECT " + filedConList[
    #                                     numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT " + str(num)
    #                                 cursor.execute(sql)
    #                                 word = ""
    #                                 for row in cursor.fetchall():
    #                                     word += "<VALUE>" + str(row[filedConList[numCon - i]]) + "</VALUE>"
    #                                 whereTemp += "<VALUES>" + str(word) + "</VALUES>"
    #                             whereTemp += "</CON>"
    #                             i -= 1
    #                         havingTemp += whereTemp
    #                         havingTemp += "</HAVING>"
    #                         new_option += havingTemp
    #                         print("HAVING ", havingTemp)
    #
    #                 if "ORDER BY" in nOpional:
    #                     orderByTemp = "<ORDERBY>"
    #                     numOrderFiled = random.randint(1, filedNum)
    #                     orderFiledList = []
    #                     values = ["ASC", "DESC"]
    #                     i = numOrderFiled
    #                     while i > 0:
    #                         randI = random.randint(0, len(listResult) - 1)
    #                         if listResult[randI] not in orderFiledList:
    #                             orderByTemp += "<FILED>"
    #                             orderFiledList.append(listResult[randI])
    #                             orderByTemp += "<FILED_NAME>" + str(listResult[randI]["COLUMN_NAME"]) + "</FILED_NAME>"
    #                             orderByTemp += "<VALUE>" + values[random.randint(0, 1)] + "</VALUE>"
    #                             orderByTemp += "</FILED>"
    #                             i -= 1
    #                     orderByTemp += "</ORDERBY>"
    #                     new_option += orderByTemp
    #
    #                 new_option += "</OPTION>"
    #                 print("OPTION : ", new_option)
    #             self.template = self.template.replace(optional, new_option)
    #
    #         if cmd.upper() == "INSERT":
    #             column = "<COLUMN><OPTION><FILED_NAME><VALUE/>[<NAME/>]</FILED_NAME></OPTION></COLUMN>"
    #             new_column = "<COLUMN><OPTION>"
    #             for filed in listResult:
    #                 new_column += "<FILED_NAME>" + filed["COLUMN_NAME"] + "</FILED_NAME>"
    #             new_column += "</OPTION></COLUMN>"
    #             self.template = self.template.replace(column, new_column)
    #
    #             values = "<VALUES>"
    #             sql = "SELECT * FROM " + table + " ORDER BY " + listResult[0]["COLUMN_NAME"] + " DESC"
    #             print(sql)
    #             cursor.execute(sql)
    #             row = cursor.fetchone()
    #             num = int(row[listResult[0]["COLUMN_NAME"]]) + 1
    #             strNum = ""
    #             if num < 10:
    #                 strNum = "00" + str(num)
    #             elif num < 100:
    #                 strNum = "0" + str(num)
    #             elif num < 100:
    #                 strNum = str(num)
    #
    #             if table != "product":
    #                 strNum = table[0:2].upper() + "-" + strNum
    #             for fileds in listResult:
    #                 filed = fileds["COLUMN_NAME"]
    #                 values += "<VALUE>"
    #                 if table == "product":
    #                     if filed == "prodNo":
    #                         values += strNum
    #                     if filed == "prodName":
    #                         values += productNameSet[random.randint(0, len(productNameSet) - 1)]
    #                     if filed == "prodPrice":
    #                         values += str(random.randint(1, 999))
    #                     if filed == "prodTotal":
    #                         values += str(random.randint(1, 100))
    #
    #                 elif table == "customer":
    #                     if filed == "custID":
    #                         values += strNum
    #                     if filed == "custName":
    #                         values += custNameSet[random.randint(0, len(custNameSet) - 1)]
    #                     if filed == "custAddr":
    #                         values += custAddrSet[random.randint(0, len(custAddrSet) - 1)]
    #                     if filed == "custProvince":
    #                         values += custProvinceSet[random.randint(0, len(custProvinceSet) - 1)]
    #                     if filed == "custPhone":
    #                         values += custPhoneSet[random.randint(0, len(custPhoneSet) - 1)]
    #
    #                 elif table == "orders":
    #                     if filed == "orderNo":
    #                         values += strNum
    #                     if filed == "orderDate":
    #                         date_time = now.strftime("%Y-%m-%d")
    #                         values += date_time
    #                     if filed == "orderTotal":
    #                         values += str(random.randint(1, 100))
    #                     if filed == "custID":
    #                         sql = "SELECT * FROM customer ORDER BY RAND() LIMIT 1"
    #                         cursor.execute(sql)
    #                         row = cursor.fetchone()
    #                         values += row['custID']
    #
    #                 elif table == "order_details":
    #                     if filed == "prodNo":
    #                         sql = "SELECT * FROM product ORDER BY RAND() LIMIT 1"
    #                         cursor.execute(sql)
    #                         row = cursor.fetchone()
    #                         values += row['prodNo']
    #                     if filed == "orderNo":
    #                         sql = "SELECT * FROM orders ORDER BY RAND() LIMIT 1"
    #                         cursor.execute(sql)
    #                         row = cursor.fetchone()
    #                         values += row['orderNo']
    #                     if filed == "quantity":
    #                         values += str(random.randint(1, 100))
    #                 values += "</VALUE>"
    #             values += "</VALUES>"
    #             self.template = self.template.replace("<VALUES/>", values)
    #
    #         if cmd.upper() == "UPDATE":
    #             values = "<VALUES>"
    #             for fileds in listResult:
    #                 filed = fileds["COLUMN_NAME"]
    #                 sql = "SELECT * FROM " + table + " ORDER BY RAND() LIMIT 1"
    #                 cursor.execute(sql)
    #                 row = cursor.fetchone()
    #                 values += "<VALUE name='" + filed + "'>" + str(row[filed]) + "(new)</VALUE>"
    #             values += "</VALUES>"
    #             whereTempOld = "<WHERE><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/><OPERATOR>=|>|<|<>|>=|<=|LIKE|BETWEEN|IN</OPERATOR><VALUE/>[<VALUE2/>][<VALUES/>]</CON></WHERE>"
    #             self.template = self.template.replace(whereTempOld, "<WHERE/>")
    #             self.template = self.template.replace("<VALUES/>", values)
    #
    #             whereTemp = "<WHERE>"
    #             numCon = random.randint(1, filedNum)
    #             filedConList = []
    #             i = numCon
    #             while i > 0:
    #                 print("LOOP5")
    #                 if listResult[numCon - i]["COLUMN_NAME"] not in filedConList:
    #                     filedConList.append(listResult[numCon - i]["COLUMN_NAME"])
    #                     i -= 1
    #             i = numCon
    #             while i > 0:
    #                 print("LOOP6")
    #                 whereTemp += "<CON>"
    #                 if i != numCon:
    #                     whereTemp += "<PRE>"
    #                     if random.randint(0, 1) == 1:
    #                         whereTemp += "AND"
    #                     else:
    #                         whereTemp += "OR"
    #                     whereTemp += "</PRE>"
    #                 whereTemp += "<FILED_NAME>" + filedConList[numCon - i] + "</FILED_NAME>"
    #                 opr = ""
    #                 oprRandI = -1
    #                 while True:
    #                     oprRandI = random.randint(0, 8)
    #                     sql = "select COUNT(*) AS NUM from information_schema.columns " \
    #                           "where table_schema = %s and TABLE_NAME = %s and COLUMN_NAME = %s and COLUMN_COMMENT LIKE %s order by table_name,ordinal_position"
    #                     queryParams = [database, table, filedConList[numCon - i],
    #                                    '%' + oprRandList[oprRandI] + '%']
    #                     cursor.execute(sql, queryParams)
    #                     row = cursor.fetchone()
    #                     if row['NUM'] > 0:
    #                         break
    #
    #                 whereTemp += "<OPERATOR>&" + oprRandList[oprRandI] + "&</OPERATOR>"
    #                 if oprRandI == 6:
    #                     sql = "SELECT " + filedConList[numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 2"
    #                     cursor.execute(sql)
    #                     word = []
    #                     for row in cursor.fetchall():
    #                         word.append(row[filedConList[numCon - i]])
    #                     whereTemp += "<VALUE>" + str(min(word)) + "</VALUE><VALUE2>" + str(max(word)) + "</VALUE2>"
    #                 elif oprRandI == 7:
    #                     word = ""
    #                     if random.randint(0, 1) == 1:
    #                         word += "%"
    #                     sql = "SELECT " + filedConList[numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 1"
    #                     cursor.execute(sql)
    #                     row = cursor.fetchone()
    #                     word += row[filedConList[numCon - i]]
    #                     if random.randint(0, 1) == 1:
    #                         word += "%"
    #                     whereTemp += "<VALUE>" + str(word) + "</VALUE>"
    #                 elif oprRandI == 8:
    #                     num = random.randint(1, 8)
    #                     sql = "SELECT " + filedConList[numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT " + str(
    #                         num)
    #                     cursor.execute(sql)
    #                     word = ""
    #                     for row in cursor.fetchall():
    #                         word += "<VALUE>" + str(row[filedConList[numCon - i]]) + "</VALUE>"
    #                     whereTemp += "<VALUES>" + str(word) + "</VALUES>"
    #                 whereTemp += "</CON>"
    #                 i -= 1
    #             whereTemp += "</WHERE>"
    #             self.template = self.template.replace("<WHERE/>", whereTemp)
    #
    #         if cmd.upper() == "DELETE":
    #             whereTemp = "<WHERE>"
    #             numCon = random.randint(1, filedNum)
    #             filedConList = []
    #             i = numCon
    #             while i > 0:
    #                 print("LOOP5")
    #                 if listColumn[numCon - i]["column_name"] not in filedConList:
    #                     filedConList.append(listColumn[numCon - i]["column_name"])
    #                     i -= 1
    #             i = numCon
    #             while i > 0:
    #                 print("LOOP6")
    #                 whereTemp += "<CON>"
    #                 if i != numCon:
    #                     whereTemp += "<PRE>"
    #                     if random.randint(0, 1) == 1:
    #                         whereTemp += "AND"
    #                     else:
    #                         whereTemp += "OR"
    #                     whereTemp += "</PRE>"
    #                 whereTemp += "<FILED_NAME>" + filedConList[numCon - i] + "</FILED_NAME>"
    #                 opr = ""
    #                 oprRandI = -1
    #                 while True:
    #                     oprRandI = random.randint(0, 8)
    #                     sql = "select COUNT(*) AS NUM from information_schema.columns " \
    #                           "where table_schema = %s and TABLE_NAME = %s and COLUMN_NAME = %s and COLUMN_COMMENT LIKE %s order by table_name,ordinal_position"
    #                     queryParams = [database, table, filedConList[numCon - i],
    #                                    '%' + oprRandList[oprRandI] + '%']
    #                     cursor.execute(sql, queryParams)
    #                     row = cursor.fetchone()
    #                     if row['NUM'] > 0:
    #                         break
    #
    #                 whereTemp += "<OPERATOR>&" + oprRandList[oprRandI] + "&</OPERATOR>"
    #                 if oprRandI == 6:
    #                     sql = "SELECT " + filedConList[numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 2"
    #                     cursor.execute(sql)
    #                     word = []
    #                     for row in cursor.fetchall():
    #                         word.append(row[filedConList[numCon - i]])
    #                     whereTemp += "<VALUE>" + str(min(word)) + "</VALUE><VALUE2>" + str(max(word)) + "</VALUE2>"
    #                 elif oprRandI == 7:
    #                     word = ""
    #                     if random.randint(0, 1) == 1:
    #                         word += "%"
    #                     sql = "SELECT " + filedConList[numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT 1"
    #                     cursor.execute(sql)
    #                     row = cursor.fetchone()
    #                     word += row[filedConList[numCon - i]]
    #                     if random.randint(0, 1) == 1:
    #                         word += "%"
    #                     whereTemp += "<VALUE>" + str(word) + "</VALUE>"
    #                 elif oprRandI == 8:
    #                     num = random.randint(1, 8)
    #                     sql = "SELECT " + filedConList[numCon - i] + " FROM " + table + " ORDER BY RAND() LIMIT " + str(
    #                         num)
    #                     cursor.execute(sql)
    #                     word = ""
    #                     for row in cursor.fetchall():
    #                         word += "<VALUE>" + str(row[filedConList[numCon - i]]) + "</VALUE>"
    #                     whereTemp += "<VALUES>" + str(word) + "</VALUES>"
    #                 whereTemp += "</CON>"
    #                 i -= 1
    #             whereTemp += "</WHERE>"
    #             whereTempOld = "<WHERE><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/><OPERATOR>=|>|<|<>|>=|<=|LIKE|BETWEEN|IN</OPERATOR><VALUE/>[<VALUE2/>][<VALUES/>]</CON></WHERE>"
    #             self.template = self.template.replace(whereTempOld, whereTemp)
    #
    #         self.template = self.template.replace("<TABLE_NAME/>", "<TABLE_NAME>" + table + "</TABLE_NAME>")
    #
    #         templateDecoder = TemplateDecoder()
    #         textDecode = templateDecoder.decode(self.template)
    #
    #         responseSuccess = textDecode
    #         return responseSuccess
    #     except Exception as e:
    #         print('TemplateService generateSelectQuestion() Exception ---> ',
    #               json.dumps(SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,
    #                                           httpError.HTTP_INTERNAL_SERVER_ERROR_MSG).__dict__))
    #         raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,
    #                                httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
    #     finally:
    #         print('Close Connection')
    #         self.cursor.close()
    #         self.con.commit()
    #         self.dbConnector.close()

    def generateQuestion(self, cmd, skillType, dbObject):
        filedExtraList = ['UPPER', 'LOWER', 'AVG', 'MIN', 'MAX', 'COUNT', 'SUM', 'FILED_NAME']
        filedExtraListWithOutCount = ['UPPER', 'LOWER', 'AVG', 'MIN', 'MAX', 'SUM', 'FILED_NAME']
        oprRandList = ["=", ">", "<", "<>", ">=", "<=", "BETWEEN", "LIKE", "IN"]
        optionalList = ["WHERE", "GROUP BY", "ORDER BY"]
        database = dbObject['name']
        self.con = self.dbConnector.connect(database)
        self.cursor = self.dbConnector.getCursor()
        try:
            listTable = dbObject['tables']
            numOfTable = len(listTable)
            randTableIndex = random.randint(0, numOfTable - 1)
            tableName = listTable[randTableIndex]['name']
            listColumn = listTable[randTableIndex]['columns']
            columnNum = len(listColumn)
            self.template = TEMPLATES[cmd.upper()][skillType.upper()]
            skillsAttr = "[remember|understand|implement|analysis]"
            self.template = self.template.replace(skillsAttr, skillType.upper())
            if cmd.upper() == 'SELECT':
                column = "<COLUMN>*|<OPTION><UPPER><FILED_NAME/>[<NAME/>]</UPPER>|<LOWER><FILED_NAME/>[<NAME/>]</LOWER>|<AVG><FILED_NAME/>[<NAME/>]</AVG>|<MIN><FILED_NAME/>[<NAME/>]</MIN>|<MAX><FILED_NAME/>[<NAME/>]</MAX>|<COUNT>*|<FILED_NAME/>[<NAME/>]</COUNT>|<SUM><FILED_NAME/>[<NAME/>]</SUM>|<FILED_NAME><VALUE/>[<NAME/>]</FILED_NAME>|<DISTINCT><FILED_NAME/>[<NAME/>]</DISTINCT></OPTION></COLUMN>"
                index = random.randint(0, 1)
                if index == 0:
                    self.template = self.template.replace(column, "<COLUMN>*</COLUMN>")
                else:
                    numOfField = random.randint(1, columnNum)
                    tempTemplate = "<COLUMN><OPTION>"
                    # Random Select in fieldExtraList
                    i = numOfField
                    colList = []
                    filedTypeList = []
                    listFieldNameWithOutCount = filedExtraListWithOutCount
                    while i > 0:
                        index = random.randint(0, columnNum - 1)
                        colList.append(listColumn[index])
                        index = random.randint(0, len(filedExtraList) - 1)
                        if filedExtraList[index] == 'COUNT':
                            if i == numOfField:  # First Element
                                filedTypeList.append(filedExtraList[index])
                                i = 0
                            else:
                                index = random.randint(0, len(listFieldNameWithOutCount) - 1)
                                filedName = listFieldNameWithOutCount[index]
                                filedTypeList.append(filedName)
                                listFieldNameWithOutCount.remove(filedName)
                        else:
                            if len(listFieldNameWithOutCount) > 0:
                                index = random.randint(0, len(listFieldNameWithOutCount) - 1)
                                filedName = listFieldNameWithOutCount[index]
                                filedTypeList.append(filedName)
                                listFieldNameWithOutCount.remove(filedName)
                            else:
                                filedTypeList.append("FILED_NAME")
                        i -= 1
                    logger.info("COLUMN LIST : " + json.dumps(colList))
                    logger.info("FILED TYPE LIST : " + json.dumps(filedTypeList))

                    for item in colList:
                        index = colList.index(item)
                        type = item['comment']['type']
                        allClause = CLAUSES[type]
                        colName = item['name']
                        asName = {
                            'UPPER': "upper_{name}", 'LOWER': "lower_{name}", 'AVG': "avg_{name}", 'MIN': "min_{name}",
                            'MAX': "max_{name}", 'COUNT': "count_{name}", 'SUM': "sum_{name}", 'FILED_NAME': ""
                        }
                        asNameSelect = asName[filedTypeList[index]].format(name=colName)
                        if filedTypeList[index] == "FILED_NAME" or filedTypeList[index] not in allClause:
                            filed = "<FILED_NAME>" + item['name'] + "</FILED_NAME>"
                        else:
                            filed = "<" + filedTypeList[index] + "><FILED_NAME>" + item[
                                'name'] + "</FILED_NAME><NAME>{nameTag}</NAME></".format(nameTag=asNameSelect) + \
                                    filedTypeList[index] + ">"
                        tempTemplate += filed
                    tempTemplate += "</OPTION></COLUMN>"
                    self.template = self.template.replace(column, tempTemplate)

            if cmd.upper() == 'INSERT':
                columnTemplate = "<COLUMN><OPTION><FILED_NAME><VALUE/>[<NAME/>]</FILED_NAME></OPTION></COLUMN>"
                tempTemplate = ""
                tempTemplate += "<COLUMN><OPTION>"
                valueTemplate = "<VALUES/>"
                valueText = "<VALUES>"
                numOfColumn = columnNum
                listSelect = []
                for i in range(numOfColumn):
                    name = listColumn[i]['name']
                    tempTemplate += "<FILED_NAME>{name}</FILED_NAME>".format(name=name)
                    valueList = listColumn[i]['comment']['exampleValue']
                    index = random.randint(0,len(valueList)-1)
                    valueText += "<VALUE>{val}</VALUE>".format(val=valueList[index])

                tempTemplate += "</OPTION></COLUMN>"
                valueText += "</VALUES>"
                self.template = self.template.replace(columnTemplate,tempTemplate)
                self.template = self.template.replace(valueTemplate,valueText)

            if cmd.upper() == 'UPDATE':
                valueTemplate = "<VALUES/>"

                sql = QUERY_COUNT_DATA(tableName)
                self.cursor.execute(sql)
                result = self.cursor.fetchone()
                count = 0
                if result:
                    count = result['NUM']

                whereClause = "<WHERE><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/><OPERATOR>=|>|<|<>|>=|<=|LIKE|BETWEEN|IN</OPERATOR><VALUE/>[<VALUE2/>][<VALUES/>]</CON></WHERE>"
                whereText = "<WHERE><CON><FILED_NAME>1</FILED_NAME><OPERATOR>&=&</OPERATOR><VALUE>1</VALUE></CON></WHERE>"
                if count > 0:
                    whereText = ""
                    preList = ["AND", "OR"]
                    whereText += "<WHERE><CON>"
                    numOfCondition = random.randint(1, columnNum)
                    i = numOfCondition
                    listColumnTemp = listTable[randTableIndex]['columns']
                    listSelect = []
                    while i > 0:
                        whereText += "<CON>"
                        if i != numOfCondition:
                            whereText += "<PRE>AND|OR</PRE>".replace("AND|OR", preList[random.randint(0, 1)])
                        index = random.randint(0, len(listColumnTemp) - 1)
                        name = listColumnTemp[index]['name']

                        if name in listSelect:
                            while name in listSelect:
                                index = random.randint(0, len(listColumnTemp) - 1)
                                name = listColumnTemp[index]['name']

                        listSelect.append(name)
                        whereText += "<FILED_NAME>{name}</FILED_NAME>".format(name=name)

                        # OPERATOR
                        index = random.randint(0, len(oprRandList) - 1)
                        opr = oprRandList[index]
                        whereText += "<OPERATOR>&{opr}&</OPERATOR>".format(opr=opr)
                        if opr == 'LIKE':
                            sql = QUERY_RAND_DATA(name, tableName, 1)
                            self.cursor.execute(sql)
                            result = self.cursor.fetchone()
                            value = ""
                            if result:
                                value = result[name]
                            whereText += "<VALUE>%{val}%</VALUE>".format(val=value)
                        elif opr == 'BETWEEN':
                            sql = QUERY_RAND_DATA(name, tableName, 2)
                            self.cursor.execute(sql)
                            result = self.cursor.fetchall()
                            value = ["", ""]
                            if result:
                                value = []
                                for item in result:
                                    value.append(result[item[name]])
                            whereText += "<VALUE1>%{val}%</VALUE1>".format(val=value[0])
                            whereText += "<VALUE2>%{val}%</VALUE2>".format(val=value[1])
                        elif opr == 'IN':
                            sql = QUERY_RAND_DATA(name, tableName, random.randint(1, 20))
                            self.cursor.execute(sql)
                            result = self.cursor.fetchall()
                            if result:
                                whereText += "<VALUES>"
                                for item in result:
                                    whereText += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                    whereText += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                whereText += "</VALUES>"
                        else:
                            sql = QUERY_RAND_DATA(name, tableName, 1)
                            self.cursor.execute(sql)
                            result = self.cursor.fetchone()
                            value = ""
                            if result:
                                value = result[name]
                            whereText += "<VALUE>{val}</VALUE>".format(val=value)
                        whereText += "</CON>"
                        i -= 1
                    whereText += "</CON></WHERE>"
                self.template = self.template.replace(whereClause, whereText)

                tempTemplate = "<VALUES>"
                numOfColumn = random.randint(1,columnNum)
                listSelect = []
                for i in range(numOfColumn):
                    index = random.randint(0,numOfColumn-1)
                    name = listColumn[index]['name']
                    valueList = listColumn[index]['comment']['exampleValue']
                    indexValue = 0
                    if name in listSelect:
                        while name in listSelect:
                            index = random.randint(0, numOfColumn - 1)
                            name = listColumn[index]['name']
                            indexValue = random.randint(0, len(valueList) - 1)
                    listSelect.append(name)
                    tempTemplate += "<VALUE name=\"{name}\">{val}</VALUE>".format(name=name,val=valueList[indexValue])
                tempTemplate += "</VALUES>"
                self.template = self.template.replace(valueTemplate, tempTemplate)

            if cmd.upper() == 'DELETE':
                sql = QUERY_COUNT_DATA(tableName)
                self.cursor.execute(sql)
                result = self.cursor.fetchone()
                count = 0
                if result:
                    count = result['NUM']

                whereClause = "<WHERE><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/><OPERATOR>=|>|<|<>|>=|<=|LIKE|BETWEEN|IN</OPERATOR><VALUE/>[<VALUE2/>][<VALUES/>]</CON></WHERE>"
                whereText = "<WHERE><CON><FILED_NAME>1</FILED_NAME><OPERATOR>&=&</OPERATOR><VALUE>1</VALUE></CON></WHERE>"
                if count > 0:
                    preList = ["AND", "OR"]
                    whereText += "<WHERE>"
                    numOfCondition = random.randint(1, columnNum)
                    i = numOfCondition
                    listColumnTemp = listTable[randTableIndex]['columns']
                    listSelect = []
                    while i > 0:
                        whereText += "<CON>"
                        if i != numOfCondition:
                            whereText += "<PRE>AND|OR</PRE>".replace("AND|OR", preList[random.randint(0, 1)])
                        index = random.randint(0, len(listColumnTemp) - 1)
                        name = listColumnTemp[index]['name']

                        if name in listSelect:
                            while name in listSelect:
                                index = random.randint(0, len(listColumnTemp) - 1)
                                name = listColumnTemp[index]['name']

                        listSelect.append(name)
                        whereText += "<FILED_NAME>{name}</FILED_NAME>".format(name=name)

                        # OPERATOR
                        index = random.randint(0, len(oprRandList) - 1)
                        opr = oprRandList[index]
                        whereText += "<OPERATOR>&{opr}&</OPERATOR>".format(opr=opr)
                        if opr == 'LIKE':
                            sql = QUERY_RAND_DATA(name, tableName, 1)
                            self.cursor.execute(sql)
                            result = self.cursor.fetchone()
                            value = ""
                            if result:
                                value = result[name]
                            whereText += "<VALUE>%{val}%</VALUE>".format(val=value)
                        elif opr == 'BETWEEN':
                            sql = QUERY_RAND_DATA(name, tableName, 2)
                            self.cursor.execute(sql)
                            result = self.cursor.fetchall()
                            value = ["", ""]
                            if result:
                                value = []
                                for item in result:
                                    value.append(result[item[name]])
                            whereText += "<VALUE1>%{val}%</VALUE1>".format(val=value[0])
                            whereText += "<VALUE2>%{val}%</VALUE2>".format(val=value[1])
                        elif opr == 'IN':
                            sql = QUERY_RAND_DATA(name, tableName, random.randint(1, 20))
                            self.cursor.execute(sql)
                            result = self.cursor.fetchall()
                            if result:
                                whereText += "<VALUES>"
                                for item in result:
                                    whereText += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                    whereText += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                whereText += "</VALUES>"
                        else:
                            sql = QUERY_RAND_DATA(name, tableName, 1)
                            self.cursor.execute(sql)
                            result = self.cursor.fetchone()
                            value = ""
                            if result:
                                value = result[name]
                            whereText += "<VALUE>{val}</VALUE>".format(val=value)
                        whereText += "</CON>"
                        i -= 1
                    whereText += "</WHERE>"
                self.template = self.template.replace(whereClause, whereText)

            isOption = random.randint(0, 1)
            optionTemplate = OPTION_TEMPLATE[skillType.upper()]
            optionTempTemplate = ""
            if isOption:
                optionTempTemplate += "<OPTION SEQ>"
                whereClause = "<WHERE><CON>[<PRE>AND|OR</PRE>]<FILED_NAME/><OPERATOR>=|>|<|<>|>=|<=|LIKE|BETWEEN|IN</OPERATOR><VALUE/>[<VALUE2/>][<VALUES/>]</CON></WHERE>"
                isWhere = random.randint(0,1)
                preList = ["AND","OR"]
                if isWhere:
                    sql = QUERY_COUNT_DATA(tableName)
                    self.cursor.execute(sql)
                    result = self.cursor.fetchone()
                    count = 0
                    if result:
                        count = result['NUM']

                    if whereClause in optionTemplate and count > 0:
                        optionTempTemplate += "<WHERE>"
                        numOfCondition = random.randint(1,columnNum)
                        i=numOfCondition
                        listColumnTemp = listTable[randTableIndex]['columns']
                        listSelect = []
                        while i > 0:
                            optionTempTemplate += "<CON>"
                            if i != numOfCondition:
                                optionTempTemplate += "<PRE>AND|OR</PRE>".replace("AND|OR",preList[random.randint(0,1)])
                            index=random.randint(0,len(listColumnTemp)-1)
                            name = listColumnTemp[index]['name']

                            if name in listSelect:
                               while name in listSelect:
                                   index = random.randint(0, len(listColumnTemp) - 1)
                                   name = listColumnTemp[index]['name']

                            listSelect.append(name)
                            optionTempTemplate += "<FILED_NAME>{name}</FILED_NAME>".format(name=name)

                            # OPERATOR
                            index = random.randint(0,len(oprRandList)-1)
                            opr = oprRandList[index]
                            optionTempTemplate += "<OPERATOR>&{opr}&</OPERATOR>".format(opr=opr)
                            if opr == 'LIKE':
                                sql = QUERY_RAND_DATA(name,tableName,1)
                                self.cursor.execute(sql)
                                result = self.cursor.fetchone()
                                value = ""
                                if result:
                                    value = result[name]
                                optionTempTemplate += "<VALUE>%{val}%</VALUE>".format(val=value)
                            elif opr == 'BETWEEN':
                                sql = QUERY_RAND_DATA(name,tableName,2)
                                self.cursor.execute(sql)
                                result = self.cursor.fetchall()
                                value = ["",""]
                                if result:
                                    value = []
                                    for item in result:
                                        value.append(result[item[name]])
                                optionTempTemplate += "<VALUE1>%{val}%</VALUE1>".format(val=value[0])
                                optionTempTemplate += "<VALUE2>%{val}%</VALUE2>".format(val=value[1])
                            elif opr == 'IN':
                                sql = QUERY_RAND_DATA(name,tableName,random.randint(1,20))
                                self.cursor.execute(sql)
                                result = self.cursor.fetchall()
                                if result:
                                    optionTempTemplate += "<VALUES>"
                                    for item in result:
                                        optionTempTemplate += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                        optionTempTemplate += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                    optionTempTemplate += "</VALUES>"
                            else:
                                sql = QUERY_RAND_DATA(name,tableName,1)
                                self.cursor.execute(sql)
                                result=self.cursor.fetchone()
                                value = ""
                                if result:
                                    value = result[name]
                                optionTempTemplate += "<VALUE>{val}</VALUE>".format(val=value)
                            optionTempTemplate += "</CON>"
                            i -= 1
                        optionTempTemplate += "</CON></WHERE>"

                isGroup = random.randint(0,1)
                groupTemplate = "<GROUPBY><FILED_NAME/></GROUPBY>"
                if isGroup and groupTemplate in optionTemplate:
                    optionTempTemplate += "<GROUPBY>"
                    numOfGroupColumn = random.randint(1,len(listColumn))
                    listColumnTemp = listColumn
                    listSelect=[]
                    for i in range(numOfGroupColumn):
                        index=0
                        index = random.randint(0,len(listColumnTemp)-1)
                        name = listColumnTemp[index]['name']

                        if name in listSelect:
                            while name in listSelect:
                                index = random.randint(0, len(listColumnTemp) - 1)
                                name = listColumnTemp[index]['name']
                        listSelect.append(name)
                        optionTempTemplate += "<FILED_NAME>{column}</FILED_NAME>".format(column=name)
                    optionTempTemplate += "</GROUPBY>"

                    isHaving = random.randint(0,1)
                    if isHaving or 1:
                        optionTempTemplate += "<HAVING><CON>"
                        numOfCondition = random.randint(1, columnNum)
                        i = numOfCondition
                        listColumnTemp = listTable[randTableIndex]['columns']
                        listSelect = []
                        while i > 0:
                            if i != numOfCondition:
                                optionTempTemplate += "<PRE>AND|OR</PRE>".replace("AND|OR",preList[random.randint(0, 1)])
                            index = 0
                            if len(listColumnTemp) > 1:
                                index = random.randint(0, len(listColumnTemp) - 1)
                            name = listColumnTemp[index]['name']
                            if name in listSelect:
                                while name in listSelect:
                                    index = random.randint(0, len(listColumnTemp) - 1)
                                    name = listColumnTemp[index]['name']
                            listSelect.append(name)
                            optionTempTemplate += "<FILED_NAME>{name}</FILED_NAME>".format(name=name)

                            # OPERATOR
                            index = random.randint(0, len(oprRandList) - 1)
                            opr = oprRandList[index]
                            optionTempTemplate += "<OPERATOR>&{opr}&</OPERATOR>".format(opr=opr)
                            if opr == 'LIKE':
                                sql = QUERY_RAND_DATA(name, tableName, 1)
                                self.cursor.execute(sql)
                                result = self.cursor.fetchone()
                                value = ""
                                if result:
                                    value = result[name]
                                optionTempTemplate += "<VALUE>%{val}%</VALUE>".format(val=value)
                            elif opr == 'BETWEEN':
                                sql = QUERY_RAND_DATA(name, tableName, 2)
                                self.cursor.execute(sql)
                                result = self.cursor.fetchall()
                                value = ["", ""]
                                if result:
                                    value = []
                                    for item in result:
                                        value.append(result[item[name]])
                                optionTempTemplate += "<VALUE1>%{val}%</VALUE1>".format(val=value[0])
                                optionTempTemplate += "<VALUE2>%{val}%</VALUE2>".format(val=value[1])
                            elif opr == 'IN':
                                sql = QUERY_RAND_DATA(name, tableName, random.randint(1, 20))
                                self.cursor.execute(sql)
                                result = self.cursor.fetchall()
                                if result:
                                    optionTempTemplate += "<VALUES>"
                                    for item in result:
                                        optionTempTemplate += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                        optionTempTemplate += "<VALUE>%{val}%</VALUE>".format(val=item[name])
                                    optionTempTemplate += "</VALUES>"
                            i -= 1

                        optionTempTemplate += "</CON></HAVING>"

                isOrder = random.randint(0,1)
                orderListValue = ["ASC","DESC"]
                orderTemplate = "<ORDERBY><FILED_NAME/><VALUE>ASC|DESC</VALUE></ORDERBY>"
                if isOrder and orderTemplate in self.template:
                    optionTempTemplate += "<ORDERBY>"
                    numOfField = random.randint(1,columnNum)
                    listSelect = []
                    for i in range(numOfField):
                        index = random.randint(0,columnNum-1)
                        name = listColumn[index]['name']
                        if name in listSelect:
                            while name in listSelect:
                                index = random.randint(0,columnNum-1)
                                name = listColumn[index]['name']

                        listSelect.append(name)
                        optionTempTemplate += "<FILED><FILED_NAME>{name}</FILED_NAME>".format(name=name)
                        optionTempTemplate += "<VALUE>{val}</VALUE></FILED>".format(val=orderListValue[random.randint(0,1)])
                    optionTempTemplate += "</ORDERBY>"
                optionTempTemplate += "</OPTION>"

            self.template = self.template.replace(optionTemplate, optionTempTemplate)

            tableNameTemplate = "<TABLE_NAME/>"
            self.template = self.template.replace(tableNameTemplate,"<TABLE_NAME>{name}</TABLE_NAME>".format(name=tableName))
            logger.info("TEMPLATE : " + self.template)

        except Exception as e:
            logger.error('TemplateService generateQuestion() Exception ---> ' + json.dumps(
                SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,
                                 httpError.HTTP_INTERNAL_SERVER_ERROR_MSG).__dict__))
            raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,
                                   httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
        finally:
            self.cursor.close()
            self.con.commit()
            self.dbConnector.close()


dbObject = {
    "name": "test",
    "tables": [{
        "name": "test_table",
        "comments": "",
        "columns": [
            {
                "name": "id",
                "comment": {
                    "name": ["ไอดี", "id"],
                    "type": "string",
                    "exampleValue": ["test-02", "test-03", "test-04", "test-05"]
                }
            },
            {
                "name": "name",
                "comment": {
                    "name": ["ชื่อ", "name"],
                    "type": "string",
                    "exampleValue": ["name", "testname", "newname", "new new"]
                }
            },
            {
                "name": "num",
                "comment": {
                    "name": ["เลข", "number"],
                    "type": "int",
                    "exampleValue": [2, 3, 4, 5, 6]
                }
            },
            {
                "name": "numDouble",
                "comment": {
                    "name": ["ดับเบิ้ล", "double"],
                    "type": "double",
                    "exampleValue": [0.12, 1.25, 225.4, 23.12345, 5432.12]
                }
            },
            {
                "name": "letter",
                "comment": {
                    "name": ["ตัวอักษร", "character"],
                    "type": "char",
                    "exampleValue": ['A', 'B', 'C', 'D', 'E', 'F']
                }
            },
            {
                "name": "date_name",
                "comment": {
                    "name": ["วันที่", "Date"],
                    "type": "date",
                    "exampleValue": ['2022-04-02', '2022-02-24', '2021-03-14', '2021-03-23']
                }
            },
            {
                "name": "dateTime_name",
                "comment": {
                    "name": ["วันเวลา", "date&time"],
                    "type": "dateTime",
                    "exampleValue": ['2021-04-25 12:22:10', '2021-09-25 10:12:12', '2021-03-31 23:59:59',
                                     '2020-12-31 01:02:03']
                }
            },
            {
                "name": "timestamp_name",
                "comment": {
                    "name": ["สแตมป์เวลา", "timestamp"],
                    "type": "timestamp",
                    "exampleValue": ['2021-04-25 12:22:10', '2021-09-25 10:12:12', '2021-03-31 23:59:59',
                                     '2020-12-31 01:02:03']
                }
            },
        ]
    }]
}
genTemplate = GenerateTemplate().generateQuestion("DELETE", "REMEMBER", dbObject)
