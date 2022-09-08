from fastapi import APIRouter, Query, Request, Form, Body
from config.db import conn
from models.index import users
from schemas.user import User
from pydantic import BaseModel

class Auth(BaseModel):
    username: str
    password: str

auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"message": "Not found"}}
)

@auth.post("/")
async def login(auth: Auth):
    return conn.execute(users.select().where(users.c.username == auth.username, users.c.password == auth.password)).fetchone()