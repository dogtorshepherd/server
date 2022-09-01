from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

exams = Table(
    'exam',meta,
    Column('exam_id',String(255),primary_key=True),
    Column('exam_db_id',String(255)),
    Column('question',String(255)),
    Column('sql',String(255)),
    Column('answer',String(255)),
    Column('score',Integer),
)