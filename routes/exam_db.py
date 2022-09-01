from fastapi import APIRouter, Query, File, UploadFile
from config.db import conn
from models.index import exam_dbs

exam_db = APIRouter(
    prefix="/exam_db",
    tags=["ExamDb"],
    responses={404: {"message": "Not found"}}
)

@exam_db.get("/")
async def read_exam_db(exam_db_id: str | None = Query(default=None, max_length=50)):
    if exam_db_id :
        return conn.execute(exam_dbs.select().where(exam_dbs.c.exam_db_id == exam_db_id)).fetchall()
    return conn.execute(exam_dbs.select()).fetchall()

@exam_db.post("/")
async def create_exam_db(exam_db_id: str, file: UploadFile = File(...)):
    conn.execute(exam_dbs.insert().values(
        exam_db_id = exam_db_id,
        source = await file.read(),
    ))
    return conn.execute(exam_dbs.select()).fetchall()

@exam_db.put("/")
async def update_exam_db(exam_db_id: str, file: UploadFile = File(...)):
    conn.execute(exam_dbs.update().values(
        exam_db_id = exam_db_id,
        source = await file.read(),
    ).where(exam_dbs.c.exam_db_id == exam_db_id))
    return conn.execute(exam_dbs.select()).fetchall()

@exam_db.delete("/")
async def delete_exam_db(exam_db_id: str):
    conn.execute(exam_dbs.delete().where(exam_dbs.c.exam_db_id == exam_db_id))
    return conn.execute(exam_dbs.select()).fetchall()