
from .product import Product

class Grass(Product):
    def __init__(self, name, description, price, quantity_in_stock, country, germination_period, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.country = country
        self.germination_period = germination_period
        self.color = color
