from abc import ABC, abstractmethod
from .utils import LogMixin, PrintMixin

class AbstractProduct(ABC, LogMixin, PrintMixin):
    @abstractmethod
    def __init__(self, name, description, price, quantity_in_stock):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = None
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена введена некорректно.")

    @price.deleter
    def price(self):
        print("Цена удалена.")

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        return cls(name, description, price, quantity_in_stock)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity_in_stock):
        super().__init__(name, description, price, quantity_in_stock)

class Smartphone(AbstractProduct):
    def __init__(self, name, description, price, quantity_in_stock, os):
        super().__init__(name, description, price, quantity_in_stock)
        self.os = os

class Grass(AbstractProduct):
    def __init__(self, name, description, price, quantity_in_stock, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.color = color
