from pydantic import BaseModel

class Sec(BaseModel):
    subject_id: str
    teacher_id: str