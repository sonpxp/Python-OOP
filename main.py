class Item:

    def __init__(self, name, price, quality):
        self.name = name
        self.price = price
        self.quality = quality

    def calculator_total_price(self):
        return self.price * self.quality


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 4)

# print(item1.name)
# print(item1.price)
# print(item1.quality)
#
# print(item2.name)
# print(item2.price)
# print(item2.quality)
print(item1.calculator_total_price())
print(item2.calculator_total_price())
