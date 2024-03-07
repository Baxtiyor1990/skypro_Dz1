
from .exceptions import ZeroQuantityException

class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__products = []

    def add_product(self, product) -> None:
        if product.quantity == 0:
            raise ValueError("Нельзя добавить товар с нулевым количеством!")
        self.__products.append(product)

    def average_price(self) -> float:
        total_price = sum([product.price for product in self.__products])
        total_quantity = sum([product.quantity for product in self.__products])

        if total_quantity == 0:
            return 0

        return total_price / total_quantity
