class SuccessClass:
    def __init__(self, message: str | None = None, data: dict | None = {}):
        self.status: bool = True
        self.message: str = message or 'Operation Succeeded'
        self.data = data
