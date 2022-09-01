from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

secs = Table(
    'sec',meta,
    Column('sec_id',String(255),primary_key=True),
    Column('subject_id',String(255)),
    Column('teacher_id',String(255)),
)