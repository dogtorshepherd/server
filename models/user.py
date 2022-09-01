from numbers import Integral
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

users = Table(
    'user',meta,
    Column('user_id',String(255),primary_key=True),
    Column('firstname',String(255)),
    Column('lastname',String(255)),
    Column('number',String(255)),
    Column('email',String(255)),
    Column('role',String(255)),
    Column('username',String(255)),
    Column('password',String(255))
)