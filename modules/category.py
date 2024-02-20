class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products or []
        Category.total_categories += 1

    def add_product(self, product):
        """Метод добавления товара в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products_info(self):
        """Геттер для вывода списка товаров"""
        products_info = []
        for product in self.__products:
            products_info.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт."
            )
        return products_info

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def __len__(self):
        return sum(product.quantity_in_stock for product in self.__products)

