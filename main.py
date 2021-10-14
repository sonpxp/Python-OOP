class Item:

    def __init__(self, name):
        self.name = name

    def calculator_total_price(self, a, b):
        return a * b


item1 = Item("Phone")
item1.price = 100
item1.quality = 5


item2 = Item("Laptop")
item2.price = 100
item2.quality = 5

print(item1.name)
print(item2.name)