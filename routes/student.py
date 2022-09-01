from fastapi import APIRouter, Query
from config.db import conn
from models.index import students
from schemas.student import Student

student = APIRouter(
    prefix="/student",
    tags=["Student"],
    responses={404: {"message": "Not found"}}
)

@student.get("/")
async def read_student(std_id: str | None = None, sec_id: str | None = None):
    if std_id and sec_id:
        return conn.execute(students.select().where(students.c.std_id == std_id, students.c.sec_id == sec_id)).fetchall()
    elif std_id :
        return conn.execute(students.select().where(students.c.std_id == std_id)).fetchall()
    elif sec_id :
        return conn.execute(students.select().where(students.c.sec_id == sec_id)).fetchall()
    else :
        return conn.execute(students.select()).fetchall()

@student.post("/")
async def create_student(student: Student):
    conn.execute(students.insert().values(
        std_id = student.std_id,
        sec_id = student.sec_id,
    ))
    return conn.execute(students.select()).fetchall()

@student.put("/")
async def update_student(student: Student):
    conn.execute(students.update().values(
        std_id = student.std_id,
        sec_id = student.sec_id,
    ).where(students.c.std_id == student.std_id))
    return conn.execute(students.select()).fetchall()