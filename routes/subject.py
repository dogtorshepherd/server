from fastapi import APIRouter, Query
from config.db import conn
from models.index import subjects
from schemas.subject import Subject

subject = APIRouter(
    prefix="/subject",
    tags=["Subject"],
    responses={404: {"message": "Not found"}}
)

@subject.get("/")
async def read_subject(subject_id: str | None = Query(default=None, max_length=50)):
    if subject_id :
        return conn.execute(subjects.select().where(subjects.c.subject_id == subject_id)).fetchall()
    return conn.execute(subjects.select()).fetchall()

@subject.post("/")
async def create_subject(subject: Subject):
    conn.execute(subjects.insert().values(
        subject_id = subject.subject_id,
        title = subject.title,
        des = subject.des,
    ))
    return conn.execute(subjects.select()).fetchall()

@subject.put("/")
async def update_subject(subject: Subject):
    conn.execute(subjects.update().values(
        subject_id = subject.subject_id,
        title = subject.title,
        des = subject.des,
    ).where(subjects.c.subject_id == subject.subject_id))
    return conn.execute(subjects.select()).fetchall()

@subject.delete("/")
async def delete_subject(subject_id: str):
    conn.execute(subjects.delete().where(subjects.c.subject_id == subject_id))
    return conn.execute(subjects.select()).fetchall()