from utils.tagParser import Stack


class TemplateDecoder:
    plainText = ""
    answer = ""
    question = ""

    def __init__(self):
        self.plainText = ""
        self.answer = ""
        self.question = ""

    def decode(self, data):
        self.plainText = data
        stack = Stack()
        selectTH = {"REMEMBER":"แสดง", "UNDERSTAND":"ดึง", "IMPLEMENT":"SELECT", "ANALYSIS":"ค้นหา"}
        insertTH = {"REMEMBER": "เพิ่ม", "UNDERSTAND": "เพิ่ม", "IMPLEMENT": "INSERT ", "ANALYSIS": "จากข้อมูลเบื้องต้น ให้เพิ่ม"}
        updateTH = {"REMEMBER": "แก้ไข", "UNDERSTAND": "แก้ไข", "IMPLEMENT": "UPDATE ", "ANALYSIS": "อัพเดท"}
        deleteTH = {"REMEMBER": "ลบ", "UNDERSTAND": "ลบ", "IMPLEMENT": "DELETE ", "ANALYSIS": "DELETE "}
        filedExtraList = ['UPPER','LOWER','AVG','MIN','MAX','COUNT','SUM','DISTINCT']
        filedExtraListTH = {"UPPER":" ตัวพิมพ์ใหญ่ของ ","LOWER":" ตัวพิมพ์เล็กของ ","AVG":" ค่าเฉลี่ยของ ","MIN":" ค่าต่ำสุดของ ","MAX":" ค่าสูงสุดของ ","COUNT":" จำนวนข้อมูลของ ","SUM":" ผลรวมของ ","DISTINCT":" DISTINCT ของ "}
        isTag = False
        isEndTag = False
        isAttrName = False
        isAttrValue = False
        isColumn = False
        isSelect = False
        isInsert = False
        isUpdate = False
        isDelete = False
        isUpper = False
        isFiledIn = False
        isLike = False
        isBetween = False
        isOrderBy = False
        isNumber = False
        isHaving = False
        isTable = False
        isOption = False
        isWhere = False
        isCon = False
        isFiledName = False
        isFiledExtra = False
        isOperator = False
        isConValue = False
        isAliasName = False
        isCompareOperator = False
        isListValue = False
        isPre = False
        isGroupBy = False
        endTag = ""
        tagName = ""
        attrName = ""
        attrValue = ""
        word = ""
        orderValue = ""
        connectWord = ""
        updateSET = ""
        opr = ""
        countI = 0
        filedNum = 0
        valueNum = 0
        filedInOrder = 0
        filedNumExtra = 0
        attr = []
        for i in self.plainText:
            word += i
            if i == "<":
                countI += 1
                isTag = True
                isEndTag = False
            elif i == ">":
                isTag = False
                isEndTag = False
                if tagName != "":
                    print("TAG ",countI," : ", tagName)
                if endTag != "":
                    print("END TAG ",countI," : ", endTag)

                if attrName != "":
                    print("Attribute: ",attrName," ==> ",attrValue)
                # START
                if tagName.upper() == "SELECT":
                    isSelect = True
                    self.answer += "SELECT"
                    self.question += selectTH[attrName.upper()]

                if tagName.upper() == "INSERT":
                    self.answer += "INSERT INTO "
                    self.question += insertTH[attrName.upper()]+"ข้อมูล"
                    isInsert = True
                if endTag.upper() == "INSERT":
                    isInsert = False

                if tagName.upper() == "UPDATE":
                    updateSET += ""
                    isUpdate = True
                    self.answer += "UPDATE "
                    self.question += updateTH[attrName.upper()]+"ข้อมูล"
                if endTag.upper() == "UPDATE":
                    self.question += " โดยมีข้อมูลดังนี้ " + updateSET
                    isUpdate = False

                if tagName.upper() == "DELETE":
                    isDelete = True
                    self.answer += "DELETE"
                    self.question += deleteTH[attrName.upper()]+"ข้อมูลทั้งหมด"
                if endTag.upper() == "DELETE":
                    isDelete = False

                if tagName.upper() == "COLUMN":
                    isColumn = True
                    if isInsert:
                        self.answer += "("
                        self.question += " โดยเพิ่มข้อมูลใส่ฟิลด์ "
                    else:
                        self.answer += " "
                    filedNum = 0
                if endTag.upper() == "COLUMN":
                    isColumn = False
                    if isInsert:
                        self.question += " ตามลำดับ"
                    filedNum = 0

                    if isInsert:
                        self.answer += ")"

                if tagName.upper() == "TABLE_NAME":
                    isTable = True
                    if not isInsert and not isUpdate:
                        self.answer += " FROM "
                        self.question += " จากตาราง "
                    if isInsert:
                        self.question += "ใส่ตาราง "
                    if isUpdate:
                        self.question += "จากตาราง "
                if endTag.upper() == "TABLE_NAME":
                    isTable = False

                if tagName.upper() == "OPTION":
                    isOption = True
                if endTag.upper() == "OPTION":
                    isOption = False

                # Extra Filed Column

                for nameExtraTag in filedExtraList:
                    if tagName.upper() == nameExtraTag:
                        isFiledExtra = True
                        if isColumn:
                            filedNumExtra += 1
                        if filedNumExtra > 1:
                            self.answer += ","
                            self.question += ","
                        elif filedNum > 0:
                            self.answer += ","
                            self.question += ","
                        self.answer += nameExtraTag+"("
                        self.question += filedExtraListTH[nameExtraTag]
                        break
                    if endTag.upper() == nameExtraTag:
                        isFiledExtra = False
                        if not isAliasName:
                            self.answer += ")"
                        isAliasName = False
                        break

                # Extra Filed Column

                if tagName.upper() == "NAME":
                    isAliasName = True
                    self.answer += ") AS "
                    self.question += " โดยใช้ชื่อ "
                # if endTag.upper() == "NAME":
                #     isAliasName = False

                if tagName.upper() == "WHERE":
                    isWhere = True
                    self.answer += " WHERE "
                    self.question += " ที่มีค่าของ "
                if endTag.upper() == "WHERE":
                    isWhere = False

                if tagName.upper() == "CON":
                    isCon = True
                if endTag.upper() == "CON":
                    isNumber = False
                    isCon = False

                if tagName.upper() == "FILED_NAME":
                    if isColumn:
                        filedNum += 1
                        if filedNum > 1 and not isFiledExtra:
                            self.answer += ","
                            self.question += ","
                            if isSelect:
                                self.question += " "
                    # if (filedNumExtra > 1 and not isFiledExtra) and isColumn:
                    #     self.answer += ","
                    #     self.question += ","
                    #     if isSelect:
                    #         self.question += " "
                    if isGroupBy:
                        filedNum += 1
                        if filedNum > 1:
                            self.answer += ","
                            self.question += ","
                    isFiledName = True
                if endTag.upper() == "FILED_NAME":
                    isFiledName = False

                if tagName.upper() == "OPERATOR":
                    isOperator = True
                    self.answer += " "
                if endTag.upper() == "OPERATOR":
                    isOperator = False

                if tagName.upper() == "VALUE":
                    if attrName == "type":
                        if attrValue == "number":
                            isNumber = True
                    isConValue = True
                    if isListValue:
                        valueNum += 1
                    if valueNum > 1:
                        self.answer += ","
                        if isUpdate and not isWhere:
                            updateSET += ","
                        else:
                            self.question += ","
                    if attrName == "name":
                        self.answer += attrValue + "="
                        updateSET += attrValue + "="
                    elif isListValue and valueNum == 1:
                        self.answer += ''
                    elif not isListValue:
                        self.answer += " "
                    if not isNumber and not isOrderBy:
                        self.answer += "'"

                if endTag.upper() == "VALUE":
                    if not isNumber and not isOrderBy:
                        self.answer += "'"
                    if orderValue == "ASC":
                        self.question += " จากน้อยไปมาก"
                    if orderValue == "DESC":
                        self.question += " จากมากไปน้อย"

                    isNumber = False
                    isConValue = False

                if tagName.upper() == "VALUE2":
                    isConValue = True
                    if attrName == "type":
                        if attrValue == "number":
                            isNumber = True
                    self.answer += " AND "
                    self.question += " ถึง "
                    if not isNumber:
                        self.answer += "'"
                if endTag.upper() == "VALUE2":
                    if not isNumber:
                        self.answer += "'"
                    isNumber = False
                    isConValue = False

                if tagName.upper() == "VALUES":
                    valueNum = 0
                    isConValue = True
                    isListValue = True
                    if isInsert:
                        self.answer += " VALUES("
                        self.question += " โดยมีค่าเท่ากับ "
                    elif isUpdate:
                        if isWhere and isCon:
                            self.answer += " ("
                            self.question += "("
                        else:
                            self.answer += " SET "
                    else:
                        self.answer += " ("
                        self.question += "("

                if endTag.upper() == "VALUES":
                    valueNum = 0
                    if isInsert:
                        self.answer += ")"
                        self.question += " ตามลำดับ"
                    if (isWhere and isCon) or isHaving:
                        self.answer += ")"
                        self.question += ")"

                    isConValue = False
                    isListValue = False

                if tagName.upper() == "PRE":
                    isPre = True
                    connectWord = ""
                    self.answer += " "
                if endTag.upper() == "PRE":
                    isPre = False
                    if connectWord.upper() == "OR":
                        self.question += " หรือ "
                    if connectWord.upper() == "AND":
                        self.question += " และ "
                    self.answer += " "

                if tagName.upper() == "GROUPBY":
                    filedNum = 0
                    isGroupBy = True
                    self.answer += " GROUP BY "
                    self.question += " โดยจัดกลุ่มตาม "
                if endTag.upper() == "GROUPBY":
                    isGroupBy = False
                    filedNum = 0

                if tagName.upper() == "HAVING":
                    isHaving = True
                    self.answer += " HAVING "
                    self.question += " ที่มีค่าของ "
                if endTag.upper() == "HAVING":
                    isHaving = False

                if tagName.upper() == "ORDERBY":
                    orderValue = ""
                    filedInOrder = 0
                    isOrderBy = True
                    self.answer += " ORDER BY "
                    self.question += " โดยให้จัดเรียงตาม "
                if endTag.upper() == "ORDERBY":
                    orderValue = ""
                    filedInOrder = 0
                    isOrderBy = False

                if tagName.upper() == "FILED":
                    filedInOrder += 1
                    if filedInOrder > 1:
                        self.answer += ","
                        self.question += ","
                        orderValue=""
                    isFiledIn = True
                if endTag.upper() == "FILED":
                    isFiledIn = False

                # CLEAR
                if not stack.isEmpty():
                    if endTag == stack.top():
                        tagNameTemp = stack.pop()
                if tagName != "":
                    stack.push(tagName)

                if attrName != "":
                    attr.append({"name": attrName, "value": attrValue})
                    isAttrValue = False
                    isAttrName = False
                    attrName = ""
                    attrValue = ""
                tagName = ""
                endTag = ""
            elif isEndTag and not isTag:
                endTag += i
            elif i == "/":
                endTag = ""
                isTag = False
                isEndTag = True
            elif i == " " and isTag:
                isAttrName = True
                print("Find!!!! Attribute")
                if attrName != "":
                    attr.append({"name": attrName, "value": attrValue})
                    isAttrValue = False
                    isAttrName = False
                    attrName = ""
                    attrValue = ""
            elif i == "=" and isTag and isAttrName:
                attrValue = ""
                isAttrValue = True
            elif isAttrValue:
                if i != "\"" and i != "\'":
                    attrValue += i
            elif isAttrName:
                if i != "\"" and i != "\'":
                    attrName += i
            elif isTag:
                tagName += i

            # LOGIC
            if i != "<" and i != "/" and i != ">" and not isTag and not isEndTag:
                if isInsert:
                    if isConValue:
                        self.answer += i
                        self.question += i
                if isDelete:
                    if isConValue and not isWhere:
                        self.answer += i
                        if isLike:
                            if i != "%":
                                self.question += i
                        else:
                            self.question += i
                    if isWhere:
                        if isCon:
                            if isPre:
                                self.answer += i
                                connectWord += i
                            if isFiledName:
                                self.answer += i
                                self.question += i
                            if isConValue:
                                self.answer += i
                                if isLike:
                                    if i != "%":
                                        self.question += i
                                else:
                                    self.question += i

                if isUpdate:
                    if isConValue and not isWhere:
                        self.answer += i
                        updateSET += i
                    if isWhere:
                        if isCon:
                            if isPre:
                                self.answer += i
                                connectWord += i
                            if isFiledName:
                                self.answer += i
                                self.question += i
                            if isConValue:
                                self.answer += i
                                if isLike:
                                    if i != "%":
                                        self.question += i
                                else:
                                    self.question += i

                if isTable:
                    self.answer += i
                    self.question += i

                if isColumn:
                    if isOption:
                        self.answer += i
                        self.question += i
                    else:
                        if i == "*":
                            self.question += " ข้อมูลทั้งหมด"
                        self.answer += i

                if isOption:
                    if isWhere or isHaving:
                        if isCon:
                            if isPre:
                                self.answer += i
                                connectWord += i
                            if isFiledName:
                                self.answer += i
                                self.question += i
                            if isConValue:
                                self.answer += i
                                if isLike:
                                    if i != "%":
                                        self.question += i
                                else:
                                    self.question += i
                    if isGroupBy:
                        if isFiledName:
                            self.answer += i
                            self.question += i

                    if isOrderBy:
                        if isFiledName:
                            self.answer += i
                            self.question += i
                        if isConValue:
                            orderValue += i
                            self.answer += i

            if isOperator:
                if i == "&":
                    if opr == "=":
                        self.question += " เป็น "
                    elif opr == ">":
                        self.question += " มากกว่า "
                    elif opr == "<":
                        self.question += " น้อยกว่า "
                    elif opr == ">=":
                        self.question += " มากกว่าเท่ากับ "
                    elif opr == "<=":
                        self.question += " น้อยกว่าเท่ากับ "
                    elif opr == "LIKE":
                        isLike = True
                        self.question += " ที่ประกอบไปด้วย "
                    elif opr == "IN":
                        self.question += " อยู่ใน "
                    elif opr == "BETWEEN":
                        isBetween = True
                        self.question += " อยู่ระหว่าง "
                    opr = ""
                    isCompareOperator = not isCompareOperator
                elif isCompareOperator:
                    self.answer += i
                    opr += i

        return {"question":self.question,"answer":self.answer,"plainText": self.plainText}

#
# "<LOWER><FILED_NAME>product_name</FILED_NAME><NAME>PRODUCT_NAME</NAME></LOWER>" \
      # "<FILED_NAME>product_name</FILED_NAME>" \
tag = "<SELECT ANALYSIS>" \
      "<COLUMN>" \
      "<OPTION>" \
      "<UPPER><FILED_NAME>product_name</FILED_NAME><NAME>PRODUCT_NAME</NAME></UPPER>" \
      "<FILED_NAME>product_name</FILED_NAME>" \
      "</OPTION>" \
      "</COLUMN>" \
      "<TABLE_NAME>product</TABLE_NAME>" \
      "<OPTION SEQ>" \
      "<WHERE>" \
      "<CON>" \
      "<FILED_NAME>product_id</FILED_NAME>" \
      "<OPERATOR>&IN&</OPERATOR>" \
      "<VALUES><VALUE>1</VALUE><VALUE>TEST</VALUE><VALUE>3</VALUE></VALUES>" \
      "</CON>" \
      "<CON>" \
      "<PRE>AND</PRE>" \
      "<FILED_NAME>product_name</FILED_NAME>" \
      "<OPERATOR>&LIKE&</OPERATOR>" \
      "<VALUE>%s%</VALUE>" \
      "</CON>" \
      "<CON>" \
      "<PRE>AND</PRE>" \
      "<FILED_NAME>product_num</FILED_NAME>" \
      "<OPERATOR>&BETWEEN&</OPERATOR>" \
      "<VALUE type=\"number\">1</VALUE>" \
      "<VALUE2>10</VALUE2>" \
      "</CON>" \
      "</WHERE>" \
      "<GROUPBY><FILED_NAME>product_id</FILED_NAME><FILED_NAME>product_name</FILED_NAME></GROUPBY>" \
      "<HAVING>" \
      "<CON>" \
      "<FILED_NAME>product_id</FILED_NAME>" \
      "<OPERATOR>&IN&</OPERATOR>" \
      "<VALUES><VALUE>1</VALUE><VALUE>TEST</VALUE><VALUE>3</VALUE></VALUES>" \
      "</CON>" \
      "<CON>" \
      "<PRE>AND</PRE>" \
      "<FILED_NAME>product_name</FILED_NAME>" \
      "<OPERATOR>&LIKE&</OPERATOR>" \
      "<VALUE>%s%</VALUE>" \
      "</CON>" \
      "</HAVING>" \
      "<ORDERBY>" \
      "<FILED>" \
      "<FILED_NAME>product_name</FILED_NAME>" \
      "<VALUE>DESC</VALUE>" \
      "</FILED>" \
      "</ORDERBY>" \
      "</OPTION>" \
      "</SELECT>"

tag = "<SELECT UNDERSTAND><COLUMN>*</COLUMN><TABLE_NAME>test_table</TABLE_NAME><OPTION SEQ><ORDERBY><FILED><FILED_NAME>name</FILED_NAME><VALUE>ASC</VALUE></FILED><FILED><FILED_NAME>id</FILED_NAME><VALUE>ASC</VALUE></FILED><FILED><FILED_NAME>date_name</FILED_NAME><VALUE>ASC</VALUE></FILED><FILED><FILED_NAME>letter</FILED_NAME><VALUE>DESC</VALUE></FILED><FILED><FILED_NAME>num</FILED_NAME><VALUE>ASC</VALUE></FILED><FILED><FILED_NAME>dateTime_name</FILED_NAME><VALUE>DESC</VALUE></FILED></ORDERBY></OPTION></SELECT>"
# tag = "<INSERT ANALYSIS>" \
#       "<TABLE_NAME>product</TABLE_NAME>" \
#       "<COLUMN>" \
#       "<OPTION>" \
#       "<FILED_NAME>product_id</FILED_NAME>" \
#       "<FILED_NAME>product_name</FILED_NAME>" \
#       "</OPTION>" \
#       "</COLUMN>" \
#       "<VALUES>" \
#       "<VALUE>1</VALUE>" \
#       "<VALUE>2</VALUE>" \
#       "</VALUES>" \
#       "</INSERT>"
#
# tag = "<UPDATE REMEMBER>" \
#       "<TABLE_NAME>product</TABLE_NAME>" \
#       "<VALUES>" \
#       "<VALUE name=\"product_id\">1</VALUE>" \
#       "<VALUE name=\"product_name\">new_product</VALUE>" \
#       "</VALUES>" \
#       "<WHERE>" \
#       "<CON>" \
#       "<FILED_NAME>product_id</FILED_NAME>" \
#       "<OPERATOR>&IN&</OPERATOR>" \
#       "<VALUES><VALUE>1</VALUE><VALUE>TEST</VALUE><VALUE>3</VALUE></VALUES>" \
#       "</CON>" \
#       "<CON>" \
#       "<PRE>AND</PRE>" \
#       "<FILED_NAME>product_name</FILED_NAME>" \
#       "<OPERATOR>&LIKE&</OPERATOR>" \
#       "<VALUE>%s%</VALUE>" \
#       "</CON>" \
#       "<CON>" \
#       "<PRE>AND</PRE>" \
#       "<FILED_NAME>product_num</FILED_NAME>" \
#       "<OPERATOR>&BETWEEN&</OPERATOR>" \
#       "<VALUE type=\"number\">1</VALUE>" \
#       "<VALUE2>10</VALUE2>" \
#       "</CON>" \
#       "</WHERE>" \
#       "</UPDATE>"
#
# tag = "<DELETE REMEMBER>" \
#       "<TABLE_NAME>product</TABLE_NAME>" \
#       "<WHERE>" \
#       "<CON>" \
#       "<FILED_NAME>product_id</FILED_NAME>" \
#       "<OPERATOR>&IN&</OPERATOR>" \
#       "<VALUES><VALUE>1</VALUE><VALUE>TEST</VALUE><VALUE>3</VALUE></VALUES>" \
#       "</CON>" \
#       "<CON>" \
#       "<PRE>AND</PRE>" \
#       "<FILED_NAME>product_name</FILED_NAME>" \
#       "<OPERATOR>&LIKE&</OPERATOR>" \
#       "<VALUE>%s%</VALUE>" \
#       "</CON>" \
#       "<CON>" \
#       "<PRE>AND</PRE>" \
#       "<FILED_NAME>product_num</FILED_NAME>" \
#       "<OPERATOR>&>=&</OPERATOR>" \
#       "<VALUE type=\"number\">1</VALUE>" \
#       "</CON>" \
#       "</WHERE>" \
#       "</DELETE>"
# tag = "<UPDATE REMEMBER><TABLE_NAME>test_table</TABLE_NAME><VALUES><VALUE name=\"name\">name</VALUE><VALUE name=\"id\">test-02</VALUE><VALUE name=\"num\">name</VALUE></VALUES><WHERE><CON><FILED_NAME>dateTime_name</FILED_NAME><OPERATOR>&>=&</OPERATOR><VALUE></VALUE></CON></WHERE></UPDATE>"
# tag = "<DELETE REMEMBER><TABLE_NAME>test_table</TABLE_NAME><WHERE><CON><FILED_NAME>1</FILED_NAME><OPERATOR>&=&</OPERATOR><VALUE>1</VALUE></CON></WHERE></DELETE>"
templateDecode = TemplateDecoder()
print(templateDecode.decode(tag))
