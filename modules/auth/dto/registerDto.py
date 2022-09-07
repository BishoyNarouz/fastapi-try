from pydantic import BaseModel


class Register(BaseModel):
    username: str
    email: str | None = None
    password: str
