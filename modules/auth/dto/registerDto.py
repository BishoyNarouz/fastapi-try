from pydantic import BaseModel, EmailStr


class RegisterDto(BaseModel):
    username: str
    password: str
    email: EmailStr
    fullName: str | None = None
