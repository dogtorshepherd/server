from fastapi import APIRouter, Query, Request, Form, Body
from config.db import conn
from models.index import users
from schemas.user import User

auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"message": "Not found"}}
)

@auth.post("/")
async def login(request: Request):
    rqJson = await request.json()
    return conn.execute(users.select().where(users.c.username == rqJson["username"], users.c.password == rqJson["password"])).fetchone()