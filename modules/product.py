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

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        return cls(name, description, price, quantity_in_stock)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            total_price = (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)
            total_quantity = self.quantity_in_stock + other.quantity_in_stock
            return total_price / total_quantity
        else:
            raise TypeError("Unsupported operand type. You can only add two Product instances.")

