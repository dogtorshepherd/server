from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

subjects = Table(
    'subject',meta,
    Column('subject_id',String(255),primary_key=True),
    Column('title',String(255)),
    Column('des',String(255))
)