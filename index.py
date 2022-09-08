from fastapi import FastAPI
from routes.index import auth, user, subject, sec, student, exam_db, exam, test, score
from fastapi.middleware.cors import CORSMiddleware

description = """
You will be able to 🚀:

* **CRUD user**
* **CRUD subject**
* **CRUD sec**
* **CRU student**
* **CRUD exam_db**
* **CRUD exam**
* **CRUD test**
* **CRU score**
"""

app = FastAPI(
    title="DB Exam",
    description=description,
    version="0.1",
)

origins = [
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:9527",
    "https://stackpython.co"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(user)
app.include_router(subject)
app.include_router(sec)
app.include_router(student)
app.include_router(exam_db)
app.include_router(exam)
app.include_router(test)
app.include_router(score)