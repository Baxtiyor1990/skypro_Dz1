from .product import AbstractProduct
class Grass(AbstractProduct):
    def __init__(self, name, description, price, quantity_in_stock, type, season, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.type = type
        self.season = season
        self.color = color
