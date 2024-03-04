from .product import Product
from .utils import LoggingMixin
from abc import ABC, abstractmethod

class OrderItem(ABC):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def calculate_total(self):
        pass

class OrderCategory(ABC):
    @abstractmethod
    def some_common_method(self):
        pass

class Order(OrderItem, OrderCategory, LoggingMixin):
    def __init__(self, product, quantity, total_cost):
        super().__init__(product, quantity)
        self.total_cost = total_cost

    def calculate_total(self):
        return self.product.price * self.quantity

    def some_common_method(self):
        print(f'This is a common method for {self.product}')

    def __repr__(self):
        return f"Order({repr(self.product)}, {self.quantity}, {self.total_cost})"
