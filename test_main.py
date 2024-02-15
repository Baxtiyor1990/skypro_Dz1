import unittest
from main import Category, Product, load_data_from_json


class TestECommerce(unittest.TestCase):

    def setUp(self):
        Category.total_categories = 0
        Category.total_products = 0

    def test_load_data_from_json(self):
        json_file_path = 'products.json'
        loaded_categories = load_data_from_json(json_file_path)

        # Проверим, что количество категорий совпадает с ожидаемым
        self.assertEqual(len(loaded_categories), 2)

        # Проверим, что количество продуктов в каждой категории совпадает с ожидаемым
        self.assertEqual(len(loaded_categories[0].get_products_info()), 2)  # Electronics
        self.assertEqual(len(loaded_categories[1].get_products_info()), 2)  # Clothing

        # Проверим, что общее количество категорий и продуктов совпадает с ожидаемым
        self.assertEqual(Category.total_categories, 2)
        self.assertEqual(Category.total_products, 4)


if __name__ == '__main__':
    unittest.main()
