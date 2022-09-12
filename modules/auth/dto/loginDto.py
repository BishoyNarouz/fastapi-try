from pydantic import BaseModel


class LoginDto(BaseModel):
    username: int
    # email: str | None = None
    password: str
