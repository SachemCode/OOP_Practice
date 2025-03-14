class Product:
    def __init__(self, name, price, cost, quantity):
        self.name = name
        self.price = price  # Selling price
        self.cost = cost  # Buying cost
        self.quantity = quantity

    def update_stock(self, amount):
        self.quantity += amount


class Department:
    def __init__(self, name):
        self.name = name


#comment 1
