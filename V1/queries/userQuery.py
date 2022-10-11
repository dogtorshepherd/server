from constants import dataTable

INSERT_USER = "INSERT INTO {table} (user_username,user_password,user_prename,user_firstname,user_lastname,user_type,user_email) VALUES(%s,%s,%s,%s,%s,%s,%s)".format(
    table=dataTable.USERS_TABLE)

EDIT_USER = "UPDATE {table} SET user_prename=%s,user_firstname=%s,user_lastname=%s,user_type=%s, updated_at=now() WHERE user_id=%s".format(
    table=dataTable.USERS_TABLE)

DELETE_USER = "DELETE FROM {table} WHERE user_id=%s".format(
    table=dataTable.USERS_TABLE)
    
INSERT_USER_ADMIN = "INSERT INTO {table} (user_username,user_password,user_prename,user_firstname,user_lastname) VALUES(%s,%s,%s,%s,%s)".format(
    table=dataTable.USERS_TABLE)
FIND_USERS = "SELECT * FROM {table} u WHERE 1=1 AND u.enable='Y'".format(table=dataTable.USERS_TABLE)


def USER_LOGIN(username, password):
    return "(SELECT u.user_id,u.user_username, u.user_firstname, u.user_lastname,u.user_prename,pt.prename_text, u.user_email, u.user_type,  " \
           "IF((SELECT COUNT(*) FROM {table} u WHERE u.user_username='{username}')>0,1,0) AS USER_EXIST , " \
           "IF((SELECT COUNT(*) FROM {table} u WHERE u.user_username = '{username}' AND u.user_password='{password}' )>0, 1,0) AS USER_LOGIN " \
           "FROM {table} u " \
           "INNER JOIN {table_prename_list} pt ON pt.prename_id = u.user_prename WHERE u.enable='Y' AND pt.enable='Y' " \
           "AND u.user_username='{username}' AND u.user_password='{password}' LIMIT 1) " \
           "".format(table=dataTable.USERS_TABLE, table_prename_list=dataTable.PRENAME_LIST_TABLE, username=username,
                     password=password)

def FIND_USERS(whereClause):
    return "SELECT * FROM {table} u WHERE 1=1 {whereClause}".format(
        user=dataTable.USERS_TABLE, whereClause=whereClause)