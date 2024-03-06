
class ZeroQuantityException(Exception):
    def __init__(self, message="Попытка добавить товар с нулевым количеством.") -> None:
        self.message = message
        super().__init__(self.message)
