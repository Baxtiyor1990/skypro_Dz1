from .product import AbstractProduct

class Smartphone(AbstractProduct):
    def __init__(self, name, description, price, quantity_in_stock, performance, model, memory, color):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
