from pydantic import BaseModel

class Exam(BaseModel):
    exam_id: str
    exam_db_id: str
    question: str
    sql: str
    answer: str
    score: int