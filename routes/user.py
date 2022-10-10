from fastapi import APIRouter, Query
from config.db import conn
from models.index import users
from schemas.user import User
from passlib.context import CryptContext

user = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"message": "Not found"}}
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@user.get("/")
async def read_user(user_id: str | None = Query(default=None, max_length=50)):
    if user_id :
        return conn.execute(users.select().where(users.c.user_id == user_id)).fetchall()
    return conn.execute(users.select()).fetchall()

@user.post("/")
async def create_user(user: User):
    conn.execute(users.insert().values(
        user_id = user.user_id,
        firstname = user.firstname,
        lastname = user.lastname,
        number = user.number,
        email = user.email,
        role = user.role,
        username = user.username,
        password = get_password_hash(user.password),
        avatar = "https://icon-library.com/images/human-icon/human-icon-22.jpg"
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/")
async def update_user(user: User):
    if user.password == "" :
        conn.execute(users.update().values(
            user_id = user.user_id,
            firstname = user.firstname,
            lastname = user.lastname,
            number = user.number,
            email = user.email,
            role = user.role,
            username = user.username,
        ).where(users.c.user_id == user.user_id))
    else :
        conn.execute(users.update().values(
            user_id = user.user_id,
            firstname = user.firstname,
            lastname = user.lastname,
            number = user.number,
            email = user.email,
            role = user.role,
            username = user.username,
            password = get_password_hash(user.password),
        ).where(users.c.user_id == user.user_id))
    return conn.execute(users.select()).fetchall()

@user.delete("/")
async def delete_user(user_id: str):
    conn.execute(users.delete().where(users.c.user_id == user_id))
    return conn.execute(users.select()).fetchall()