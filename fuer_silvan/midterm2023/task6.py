class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def __str__(self):
        return f"{self.name} sells for {self.price:.2f}"

    def __repr__(self):
        return f"Product({self.name}, {self.price:.2f}, {self.discount:.2f}"

    def sales_price(self):
        return round(self.price - self.price*self.discount, 2)


p = Product("Smartphone", 1000, 0.1)
print(p.sales_price())
print(p)
print([p, Product("Dumbphone", 100, 0.2)])
