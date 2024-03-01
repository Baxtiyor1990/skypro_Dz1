from .product import AbstractProduct

class Order(AbstractProduct):
    def __init__(self):
        super().__init__("Order", "Заказ", 0, 0)
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Добавление продукта {product.name} в заказ.")

