
from abc import ABC, abstractmethod
from .exceptions import ZeroQuantityException

class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass


class Product(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ZeroQuantityException()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n'

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)
