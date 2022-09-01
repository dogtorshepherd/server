from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

scores = Table(
    'score',meta,
    Column('std_id',String(255)),
    Column('exam_id',String(255)),
    Column('score',Integer),
)