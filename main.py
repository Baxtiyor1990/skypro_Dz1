from modules.category import Category
from modules.smartphone import Smartphone
from modules.grass import Grass
from modules.order import Order
from modules.utils import LogMixin, PrintMixin

iphone = Smartphone("iPhone", "Smartphone", 1000, 10, "High", "X", "256GB", "Silver", "iOS")
bluegrass = Grass("Bluegrass", "Grass", 5, 100, "Country", "Spring", "Blue")

phones_category = Category("Phones", "Smartphones and accessories")
lawns_category = Category("Lawns", "Grass and gardening")

phones_category.add_product(iphone)
lawns_category.add_product(bluegrass)

order = Order()
order.add_product(iphone)
order.add_product(bluegrass)

print("Категории:")
print(phones_category)
print(lawns_category)

print("\nЗаказ:")
print(order)
