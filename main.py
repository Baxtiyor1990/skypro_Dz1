from modules.category import Category, Order
from modules.product import Smartphone, Grass

iphone = Smartphone("iPhone", "Smartphone", 1000, 10, "iOS")
bluegrass = Grass("Bluegrass", "Grass", 5, 100, "Blue")

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
