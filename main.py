import json


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        """Метод для добавления товара в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    def get_products_info(self):
        """Геттер для вывода списка товаров"""
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.")
        return products_info


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.__price = None
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена введена некорректно.")

    @price.deleter
    def price(self):
        print("Цена удалена.")
        del self.__price


def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    categories = []
    for category_data in data['categories']:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity_in_stock']
            )
            category.add_product(product)
        categories.append(category)

    return categories


if __name__ == "__main__":
    # Загружаем данные из файла JSON
    json_file_path = 'products.json'
    loaded_categories = load_data_from_json(json_file_path)

    # Вывод информации о категориях и их продуктах
    for category in loaded_categories:
        print(f"\nCategory: {category.name}")
        print(f"Description: {category.description}")
        print("Products:")
        for product_info in category.get_products_info():
            print(f"\t{product_info}")

