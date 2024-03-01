import unittest
from modules.category import Category, Order
from modules.product import Smartphone, Grass

class TestECommerce(unittest.TestCase):
    def setUp(self):
        Category.total_categories = 0
        Category.total_products = 0

    def test_category_initialization(self):
        category = Category("Phones", "Smartphones and accessories")
        self.assertEqual(category.name, "Phones")
        self.assertEqual(category.description, "Smartphones and accessories")
        self.assertEqual(len(category.products_info), 0)
        self.assertEqual(Category.total_categories, 1)

    def test_product_initialization(self):
        iphone = Smartphone("iPhone", "Smartphone", 1000, 10, "iOS")
        self.assertEqual(iphone.name, "iPhone")
        self.assertEqual(iphone.description, "Smartphone")
        self.assertEqual(iphone.price, 1000)
        self.assertEqual(iphone.quantity_in_stock, 10)

    def test_add_product_to_category(self):
        phones_category = Category("Phones", "Smartphones and accessories")
        iphone = Smartphone("iPhone", "Smartphone", 1000, 10, "iOS")
        phones_category.add_product(iphone)
        self.assertEqual(len(phones_category.products_info), 1)
        self.assertEqual(Category.total_products, 1)

    def test_order_initialization(self):
        order = Order()
        self.assertEqual(len(order.products_info), 0)

    def test_add_product_to_order(self):
        order = Order()
        iphone = Smartphone("iPhone", "Smartphone", 1000, 10, "iOS")
        order.add_product(iphone)
        self.assertEqual(len(order.products_info), 1)

if __name__ == '__main__':
    unittest.main()

