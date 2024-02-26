from modules.category import Category
from modules.product import Product
from modules.smartphone import Smartphone
from modules.grass import Grass
from modules.utils import load_data_from_json

# Загружаем данные из файла JSON
json_file_path = 'products.json'
loaded_categories = load_data_from_json(json_file_path)

# Вывод информации о категориях и их продуктах
for category in loaded_categories:
    print(f"\nCategory: {category.name}")
    print(f"Description: {category.description}")
    print("Products:")
    for product_info in category.products_info:
        print(f"\t{product_info}")
