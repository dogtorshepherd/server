from pydantic import BaseModel

class Sec(BaseModel):
    sec_id: int
    subject_id: str
    teacher_id: str