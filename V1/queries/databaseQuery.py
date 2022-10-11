from constants import dataTable

FIND_ALL_DATABASE = "SELECT * FROM {table} d WHERE d.enable='Y'".format(table=dataTable.SYSTEM_DATABASES_TABLE)
INSERT_DATABASE = "INSERT INTO {table} (database_name) VALUES(%s)".format(table=dataTable.SYSTEM_DATABASES_TABLE)
UPDATE_DATABASE = "UPDATE {table} SET database_name=%s WHERE database_id=%s".format(table=dataTable.SYSTEM_DATABASES_TABLE)
DELETE_DATABASE = "DELETE FROM {table} WHERE database_id=%s".format(table=dataTable.SYSTEM_DATABASES_TABLE)

def FIND_INFO_DATABASE(whereClause) :
    return "SELECT * FROM {table} d WHERE d.enable='Y' {whereClause}".format(table=dataTable.SYSTEM_DATABASES_TABLE, whereClause=whereClause)