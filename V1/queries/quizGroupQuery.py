from constants import dataTable

FIND_ALL_QUIZ_GROUP = "SELECT \
    qg.quiz_group_id, \
    qg.database_id, \
    qg.quiz_objective, \
    qg.quiz_num,\
    qg.quiz_type,\
    DATE_FORMAT(qg.quiz_start_date, '%y-%m-%d') AS quiz_start_date,\
    DATE_FORMAT(qg.quiz_end_date, '%y-%m-%d') AS quiz_end_date,\
    DATE_FORMAT(qg.quiz_start_time, '%h:%i:%s') AS quiz_start_time,\
    DATE_FORMAT(qg.quiz_end_time, '%h:%i:%s') AS quiz_end_time,\
    sd.database_id,\
    sd.database_name \
FROM \
    {table} qg \
INNER JOIN system_databases sd ON sd.database_id = qg.database_id \
WHERE qg.enable='Y';".format(table=dataTable.QUIZ_GROUP_TABLE)

FIND_INFO_QUIZ_GROUP = "SELECT \
    qg.quiz_group_id, \
    qg.database_id, \
    qg.quiz_objective, \
    qg.quiz_num,\
    qg.quiz_type,\
    DATE_FORMAT(qg.quiz_start_date, '%y-%m-%d') AS quiz_start_date,\
    DATE_FORMAT(qg.quiz_end_date, '%y-%m-%d') AS quiz_end_date,\
    DATE_FORMAT(qg.quiz_start_time, '%h:%i:%S') AS quiz_start_time,\
    DATE_FORMAT(qg.quiz_end_time, '%h:%i:%S') AS quiz_end_time,\
    sd.database_id,\
    sd.database_name \
FROM \
    {table} qg \
INNER JOIN system_databases sd ON sd.database_id = qg.database_id \
WHERE qg.enable='Y' AND qg.quiz_group_id=%s".format(table=dataTable.QUIZ_GROUP_TABLE)

INSERT_QUIZ_GROUP = "INSERT INTO {table} (`database_id`, `quiz_objective`, `quiz_num`, `quiz_type`, `quiz_start_date`, `quiz_end_date`, `quiz_start_time`, `quiz_end_time`, `subject_group_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);".format(
    table=dataTable.QUIZ_GROUP_TABLE)

UPDATE_QUIZ_GROUP = "UPDATE {table} SET `database_id`=%s,`quiz_objective`=%s, `quiz_num`=%s, `quiz_type`=%s, `quiz_start_date`=%s, `quiz_end_date`=%s, `quiz_start_time`=%s, `quiz_end_time`=%s, `subject_group_id`=%s WHERE quiz_group_id=%s".format(
    table=dataTable.QUIZ_GROUP_TABLE)

DELETE_QUIZ_GROUP = "DELETE FROM {table} WHERE quiz_group_id=%s".format(table=dataTable.QUIZ_GROUP_TABLE)
