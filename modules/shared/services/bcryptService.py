from passlib.context import CryptContext


async def hashPassword(password: str) -> str:
    return CryptContext(schemes=["bcrypt"], deprecated="auto", round=12).hash(password)


async def comparePassword(password: str, hashedPassword: str) -> bool:
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(password, hashedPassword)
