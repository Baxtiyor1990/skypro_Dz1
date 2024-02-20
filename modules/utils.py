import json
from .category import Category
from .product import Product

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    categories = []
    for category_data in data['categories']:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product.create_product(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity_in_stock']
            )
            category.add_product(product)
        categories.append(category)

    return categories
