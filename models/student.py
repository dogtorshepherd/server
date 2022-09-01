from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

students = Table(
    'student',meta,
    Column('std_id',String(255)),
    Column('sec_id',String(255)),
)