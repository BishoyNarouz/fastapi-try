from passlib.context import CryptContext


class PasswordService:

    def hashPassword(self, password: str) -> str:
        return CryptContext(schemes=["bcrypt"], deprecated="auto",).hash(password)

    def comparePassword(self, password: str, hashedPassword: str) -> bool:
        return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(password, hashedPassword)
