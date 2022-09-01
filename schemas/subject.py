from pydantic import BaseModel

class Subject(BaseModel):
    subject_id: str
    title: str
    des: str