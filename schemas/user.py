from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    firstname: str
    lastname: str
    number: str | None = None
    email: str | None = None
    role: str
    username: str
    password: str
    bio: str | None = None
    avatar: str | None = None
    disabled: bool | None = None