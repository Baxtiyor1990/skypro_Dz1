from .product import AbstractProduct

class Grass(AbstractProduct):
    def __init__(self, name, description, price, quantity_in_stock, country, germination_period, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def specific_method(self):
        # Добавьте реализацию конкретного метода для травы, если необходимо
        pass
