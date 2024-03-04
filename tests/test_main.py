import unittest
from modules.smartphone import Smartphone
from modules.grass import LawnGrass
from modules.order import Order

class TestMain(unittest.TestCase):
    def test_smartphone_repr(self):
        smartphone = Smartphone('iPhone', 'Smartphone description', 1000, 5, 'iPhone X')
        expected_repr = "Smartphone('iPhone', 'Smartphone description', 1000, 5, 'iPhone X')"
        self.assertEqual(repr(smartphone), expected_repr)

    def test_lawn_grass_repr(self):
        lawn_grass = LawnGrass('Grass', 'Lawn grass description', 20, 100, 'Ryegrass')
        expected_repr = "LawnGrass('Grass', 'Lawn grass description', 20, 100, 'Ryegrass')"
        self.assertEqual(repr(lawn_grass), expected_repr)

    def test_order_repr(self):
        smartphone = Smartphone('iPhone', 'Smartphone description', 1000, 5, 'iPhone X')
        order = Order(smartphone, 2, 2000)
        expected_repr = "Order(Smartphone('iPhone', 'Smartphone description', 1000, 5, 'iPhone X'), 2, 2000)"
        self.assertEqual(repr(order), expected_repr)

if __name__ == '__main__':
    unittest.main()

