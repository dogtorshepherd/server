from constants import dataTable

FIND_ALL_MAJOR = "SELECT * FROM {table} WHERE enable='Y'".format(table=dataTable.MAJOR_TABLE)