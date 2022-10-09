from fastapi import APIRouter, Query
from config.db import conn
from models.index import exams
from schemas.exam import Exam

exam = APIRouter(
    prefix="/exam",
    tags=["Exam"],
    responses={404: {"message": "Not found"}}
)

@exam.get("/")
async def read_exam(sec_id: str | None = Query(default=None, max_length=50), exam_id: str | None = Query(default=None, max_length=50)):
    if sec_id :
        # print("sec_id : " + sec_id)
        return conn.execute(exams.select().where(exams.c.sec_id == sec_id)).fetchall()
    if exam_id :
        return conn.execute(exams.select().where(exams.c.exam_id == exam_id)).fetchone()
    return conn.execute(exams.select()).fetchall()

@exam.post("/")
async def create_exam(exam: Exam):
    conn.execute(exams.insert().values(
        sec_id = exam.sec_id,
        question = exam.question,
        answer = exam.answer,
        score = exam.score,
    ))
    return conn.execute(exams.select()).fetchall()

@exam.put("/")
async def update_exam(exam: Exam):
    conn.execute(exams.update().values(
        question = exam.question,
        answer = exam.answer,
        score = exam.score,
    ).where(exams.c.exam_id == exam.exam_id))
    return conn.execute(exams.select()).fetchall()

@exam.delete("/")
async def delete_exam(exam_id: str):
    conn.execute(exams.delete().where(exams.c.exam_id == exam_id))
    return conn.execute(exams.select()).fetchall()