
from .product import Product
from .utils import LoggingMixin

class LawnGrass(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, grass_type):
        super().__init__(name, description, price, quantity)
        self.grass_type = grass_type

    def some_abstract_method(self):
        print(f'This is a specific method for {self.name}')

    def __repr__(self):
        return super().__repr__()
