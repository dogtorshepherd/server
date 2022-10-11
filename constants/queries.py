def QUERY_RAND_DATA(colunStr,table,num):
    return "SELECT {colunStr} FROM {table} ORDER BY RAND() LIMIT {num}".format(colunStr=colunStr,table=table,num=num)

def QUERY_COUNT_DATA(table):
    return "SELECT COUNT(*) AS NUM FROM {table}".format(table=table)