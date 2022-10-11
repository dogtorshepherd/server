from constants import dataTable
FIND_ALL_QUESTION = "SELECT q.quiz_question,q.quiz_answer,q.quiz_point,q.quiz_standard FROM {table} q INNER JOIN {join_table} qg ON qg.quiz_group_id = q.quiz_group_id WHERE qg.enable='Y' AND qg.quiz_group_id=%s".format(table=dataTable.QUIZ_TABLE, join_table=dataTable.QUIZ_GROUP_TABLE)
INSERT_QUIZ = "INSERT INTO {table} (`quiz_question`, `quiz_answer`, `quiz_point`, `quiz_standard`, `quiz_group_id`) VALUES (%s, %s, %s, %s, %s)".format(table=dataTable.QUIZ_TABLE)
UPDATE_QUIZ = "UPDATE {table} SET `quiz_question`=%s, `quiz_answer`=%s, `quiz_point`=%s, `quiz_standard`=%s, `quiz_group_id`=%s WHERE quiz_id=%s".format(table=dataTable.QUIZ_TABLE)
DELETE_QUIZ = "DELETE FROM {table} WHERE quiz_id=%s".format(table=dataTable.QUIZ_TABLE)
