
class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products = []

    def calculate_average_price(self):
        try:
            total_price = sum(product.price for product in self.products)
            average_price = total_price / len(self.products)
        except ZeroDivisionError:
            return 0
        return average_price
