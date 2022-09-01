from pydantic import BaseModel

class Test(BaseModel):
    test_id: str
    exam_db_id: str
    sec_id: str