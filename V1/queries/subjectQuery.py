from constants import dataTable

INSERT_SUBJECT = "INSERT INTO {table} (subject_code, subject_name, subject_decription, subject_year, course_id, enable) VALUES(%s,%s,%s,%s,%s,%s)".format(
    table=dataTable.SUBJECTS_TABLE)

EDIT_SUBJECT = "UPDATE {table} SET subject_code=%s, subject_name=%s, subject_decription=%s, subject_year=%s, course_id=%s, enable=%s WHERE subject_id=%s".format(
    table=dataTable.SUBJECTS_TABLE)

DELETE_SUBJECT = "DELETE FROM {table} WHERE subject_id=%s".format(
    table=dataTable.SUBJECTS_TABLE)

def FIND_ALL_SUBJECT(whereClause):
    return "SELECT * FROM {table} s INNER JOIN {courses} c ON s.course_id = c.course_id WHERE 1=1 {whereClause}".format(
        table=dataTable.SUBJECTS_TABLE, courses=dataTable.COURSES_TABLE,whereClause=whereClause)