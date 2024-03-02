from modules.utils import LogMixin, PrintMixin

class Order(LogMixin, PrintMixin):
    def __init__(self):
        super().__init__()
        self.products_info = []

    def add_product(self, product):
        self.log(f"Добавление продукта {product.name} в заказ.")
        self.products_info.append(product)

    def __str__(self):
        return f"Заказ, Лог: {', '.join(self.log_messages)}"
