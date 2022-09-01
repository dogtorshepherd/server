from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

tests = Table(
    'test',meta,
    Column('test_id',String(255),primary_key=True),
    Column('exam_db_id',String(255)),
    Column('sec_id',String(255)),
)