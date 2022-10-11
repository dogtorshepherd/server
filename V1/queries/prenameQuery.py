from constants import dataTable

FIND_ALL_PRENAMES = "SELECT * FROM {table} WHERE enable='Y'".format(table=dataTable.PRENAME_LIST_TABLE)