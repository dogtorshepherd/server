from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

exams = Table(
    'exam',meta,
    Column('exam_id',Integer,primary_key=True),
    Column('sec_id',Integer),
    Column('question',String(255)),
    Column('answer',String(255)),
    Column('score',Integer),
)