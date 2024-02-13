import unittest
from main import Category, Product

class TestECommerce(unittest.TestCase):

    def setUp(self):
        Category.total_categories = 0
        Category.total_products = 0

    def test_category_initialization(self):
        category = Category("Electronics", "Electronics category description")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronics category description")
        self.assertEqual(len(category.products), 0)
        self.assertEqual(Category.total_categories, 1)

    def test_product_initialization(self):
        product = Product("Laptop", "Powerful laptop", 1200.50, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "Powerful laptop")
        self.assertEqual(product.price, 1200.50)
        self.assertEqual(product.quantity_in_stock, 10)

    def test_add_product_to_category(self):
        category = Category("Electronics", "Electronics category description")
        product = Product("Laptop", "Powerful laptop", 1200.50, 10)
        category.add_product(product)
        self.assertEqual(len(category.products), 1)
        self.assertEqual(Category.total_products, 1)

    def test_total_categories_and_products(self):
        category1 = Category("Electronics", "Electronics category description")
        product1 = Product("Laptop", "Powerful laptop", 1200.50, 10)
        category1.add_product(product1)

        category2 = Category("Clothing", "Clothing category description")
        product2 = Product("T-shirt", "Cotton T-shirt", 19.99, 50)
        category2.add_product(product2)

        self.assertEqual(Category.total_categories, 2)
        self.assertEqual(Category.total_products, 2)

if __name__ == '__main__':
    unittest.main()
