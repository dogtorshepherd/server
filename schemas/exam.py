from pydantic import BaseModel

class Exam(BaseModel):
    exam_id: int
    sec_id: str
    question: str
    answer: str
    score: int