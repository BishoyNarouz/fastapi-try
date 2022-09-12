from datetime import datetime


class ErrorClass:
    def __init__(self, statusCode: int, errors: list(str) | None = []):
        self.status: bool = False
        self.errors: list(str) = errors
        self.timeStamp = datetime
