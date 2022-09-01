from pydantic import BaseModel

class Score(BaseModel):
    std_id: str
    exam_id: str
    score: int