import json

class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.total_products += 1

class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

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

# Загружаем данные из файла JSON
json_file_path = 'products.json'
loaded_categories = load_data_from_json(json_file_path)

# Вывод информации о категориях и их продуктах
for category in loaded_categories:
    print(f"\nCategory: {category.name}")
    print(f"Description: {category.description}")
    print("Products:")
    for product in category.products:
        print(f"\tProduct: {product.name}")
        print(f"\tDescription: {product.description}")
        print(f"\tPrice: ${product.price}")
        print(f"\tQuantity in stock: {product.quantity_in_stock}\n")
