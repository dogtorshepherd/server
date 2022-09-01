from pydantic import BaseModel

class Student(BaseModel):
    std_id: str
    sec_id: str