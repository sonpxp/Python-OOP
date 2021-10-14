class Item:
    # can set default = 0 ex: quality = 0
    pay_rate = 0.8

    def __init__(self, name, price, quality):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quality >= 0, f"quality {quality} is not greater than or equal to zero!"

        # assert to self object
        self.name = name
        self.price = price
        self.quality = quality

    def calculator_total_price(self):
        return self.price * self.quality

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 4)

print(Item.__dict__) # All the attributes for class level
print(item1.__dict__) # All the attributes for instance level
print(item2.__dict__)

# print(item1.calculator_total_price())
# print(item2.calculator_total_price())

# print(item1.name)
# print(item1.price)
# print(item1.quality)
#
# print(item2.name)
# print(item2.price)
# print(item2.quality)

