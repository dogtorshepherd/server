from constants import dataTable

FIND_ALL_ADMIN = "SELECT * FROM {table} t INNER JOIN {user} u ON u.user_id = t.user_id WHERE u.enable='Y'".format(table=dataTable.ADMIN_TABLE,user=dataTable.USERS_TABLE)
INSERT_ADMIN = "INSERT INTO {table} (user_id,admin_id) VALUES(%s,%s)".format(table=dataTable.ADMIN_TABLE)
EDIT_ADMIN = "UPDATE {table} SET admin_id = %s WHERE user_id=%s ".format(table=dataTable.ADMIN_TABLE)
UPDATE_ADMIN = "UPDATE {table} u SET u.enable=now(),u.updated_at=%s WHERE u.user_id=%s".format(table=dataTable.ADMIN_TABLE)

def FIND_ADMIN_WHERE_CLAUSE(clause):
    return "SELECT * FROM {table} t INNER JOIN {user} u ON u.user_id = t.user_id WHERE 1=1 AND u.enable='Y' {clause}".format(table=dataTable.ADMIN_TABLE, user=dataTable.USERS_TABLE, clause=clause)