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
