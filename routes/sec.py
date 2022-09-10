from fastapi import APIRouter, Query
from config.db import conn
from models.index import secs
from schemas.sec import Sec

sec = APIRouter(
    prefix="/sec",
    tags=["Sec"],
    responses={404: {"message": "Not found"}}
)

@sec.get("/")
async def read_sec(sec_id: str | None = Query(default=None, max_length=50)):
    if sec_id :
        return conn.execute(secs.select().where(secs.c.sec_id == sec_id)).fetchall()
    return conn.execute(secs.select()).fetchall()

@sec.post("/")
async def create_sec(sec: Sec):
    conn.execute(secs.insert().values(
        subject_id = sec.subject_id,
        teacher_id = sec.teacher_id,
    ))
    return conn.execute(secs.select()).fetchall()

@sec.put("/")
async def update_sec(sec: Sec):
    conn.execute(secs.update().values(
        sec_id = sec.sec_id,
        subject_id = sec.subject_id,
        teacher_id = sec.teacher_id,
    ).where(secs.c.sec_id == sec.sec_id))
    return conn.execute(secs.select()).fetchall()

@sec.delete("/")
async def delete_sec(sec_id: str):
    conn.execute(secs.delete().where(secs.c.sec_id == sec_id))
    return conn.execute(secs.select()).fetchall()