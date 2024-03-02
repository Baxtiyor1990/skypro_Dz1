from .utils import LogMixin, PrintMixin

class Category(LogMixin, PrintMixin):
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.products_info = []
        Category.total_categories += 1

    def add_product(self, product):
        self.log(f"Добавление продукта {product.name} в категорию.")
        self.products_info.append(product)
        Category.total_products += 1

    def __str__(self):
        return f"{self.name}, {self.description}, Лог: {', '.join(self.log_messages)}"
