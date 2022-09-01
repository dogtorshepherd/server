from fastapi import APIRouter, Query
from config.db import conn
from models.index import tests
from schemas.test import Test

test = APIRouter(
    prefix="/test",
    tags=["Test"],
    responses={404: {"message": "Not found"}}
)

@test.get("/")
async def read_test(test_id: str | None = Query(default=None, max_length=50)):
    if test_id :
        return conn.execute(tests.select().where(tests.c.test_id == test_id)).fetchall()
    return conn.execute(tests.select()).fetchall()

@test.post("/")
async def create_test(test: Test):
    conn.execute(tests.insert().values(
        test_id = test.test_id,
        exam_db_id = test.exam_db_id,
        sec_id = test.sec_id,
    ))
    return conn.execute(tests.select()).fetchall()

@test.put("/")
async def update_test(test: Test):
    conn.execute(tests.update().values(
        test_id = test.test_id,
        exam_db_id = test.exam_db_id,
        sec_id = test.sec_id,
    ).where(tests.c.test_id == test.test_id))
    return conn.execute(tests.select()).fetchall()

@test.delete("/")
async def delete_test(test_id: str):
    conn.execute(tests.delete().where(tests.c.test_id == test_id))
    return conn.execute(tests.select()).fetchall()