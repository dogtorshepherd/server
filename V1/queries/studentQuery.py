from constants import dataTable

FIND_ALL_USERS_BY_GROUP_ID = "SELECT * FROM {table} t INNER JOIN {user} u ON u.user_id = t.user_id " \
                             "INNER JOIN {subject_group} sg ON sg.user_id_teacher = u.user_id " \
                             "WHERE u.enable='Y' AND sg.subject_group_id = %s" \
                             "".format(table=dataTable.STUDENTS_TABLE,user=dataTable.USERS_TABLE,subject_group=dataTable.SUBJECT_GROUPS_TABLE)

INSERT_STUDENT = "INSERT INTO {table} (user_id,student_id,major_id) VALUES(%s,%s,%s)".format(table=dataTable.STUDENTS_TABLE)
EDIT_STUDENT = "UPDATE {table} SET student_id=%s,major_id=%s WHERE user_id=%s".format(table=dataTable.STUDENTS_TABLE)
FIND_ALL_STUDENTS = "SELECT * FROM {table} s INNER JOIN {user_table} u ON u.user_id = s.user_id WHERE u.enable='Y'".format(table=dataTable.STUDENTS_TABLE, user_table=dataTable.USERS_TABLE)
def FIND_STUDENT(whereClause='') :
    return "SELECT * FROM {table} s INNER JOIN {user_table} u ON u.user_id = s.user_id WHERE u.enable='Y' {whereClause} ".format(table=dataTable.STUDENTS_TABLE, user_table=dataTable.USERS_TABLE, whereClause=whereClause)