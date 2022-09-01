from fastapi import APIRouter, Query
from config.db import conn
from models.index import scores
from schemas.score import Score

score = APIRouter(
    prefix="/score",
    tags=["Score"],
    responses={404: {"message": "Not found"}}
)

@score.get("/")
async def read_score(std_id: str | None = None, exam_id: str | None = None):
    if std_id and exam_id:
        return conn.execute(scores.select().where(scores.c.std_id == std_id, scores.c.exam_id == exam_id)).fetchall()
    elif std_id :
        return conn.execute(scores.select().where(scores.c.std_id == std_id)).fetchall()
    elif exam_id :
        return conn.execute(scores.select().where(scores.c.exam_id == exam_id)).fetchall()
    else :
        return conn.execute(scores.select()).fetchall()

@score.post("/")
async def create_score(score: Score):
    conn.execute(scores.insert().values(
        std_id = score.std_id,
        exam_id = score.exam_id,
        score = score.score,
    ))
    return conn.execute(scores.select()).fetchall()

@score.put("/")
async def update_score(score: Score):
    conn.execute(scores.update().values(
        score = score.score,
    ).where(scores.c.std_id == score.std_id, scores.c.exam_id == score.exam_id))
    return conn.execute(scores.select()).fetchall()