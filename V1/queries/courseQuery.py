from constants import dataTable

FIND_ALL_COURSE = "SELECT * FROM {table} WHERE enable='Y'".format(table=dataTable.COURSES_TABLE)