from pydantic import BaseModel

class Sec(BaseModel):
    sec_id: str
    subject_id: str
    teacher_id: str