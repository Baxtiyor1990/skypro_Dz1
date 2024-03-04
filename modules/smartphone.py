
from .product import Product
from .utils import LoggingMixin

class Smartphone(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, model):
        super().__init__(name, description, price, quantity)
        self.model = model

    def some_abstract_method(self):
        print(f'This is a specific method for {self.name}')

    def __repr__(self):
        return super().__repr__()
