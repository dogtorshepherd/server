from constants import dataTable


def FIND_ALL_TEACHERS(whereClause):
    return "SELECT * FROM {table} t INNER JOIN {user} u ON u.user_id = t.user_id INNER JOIN {prename} p ON p.prename_id = u.user_prename WHERE u.enable='Y' {whereClause}".format(
        table=dataTable.TEACHERS_TABLE, user=dataTable.USERS_TABLE, prename=dataTable.PRENAME_LIST_TABLE,whereClause=whereClause)


INSERT_TEACHER = "INSERT INTO {table} (user_id,teacher_id,teacher_phone) VALUES(%s,%s,%s)".format(
    table=dataTable.TEACHERS_TABLE)

EDIT_TEACHER = "UPDATE {table} SET teacher_id=%s,teacher_phone=%s WHERE user_id=%s".format(
    table=dataTable.TEACHERS_TABLE)
