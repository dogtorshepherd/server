from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,BLOB
from config.db import meta

exam_dbs = Table(
    'exam_db',meta,
    Column('exam_db_id',String(255),primary_key=True),
    Column('source',BLOB),
)