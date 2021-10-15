class Item:
    # can set default = 0 ex: quantity = 0
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"

        # assert to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculator_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  # Item.pay_rate

    def __repr__(self):
        return f"Item '{self.name}, {self.price}, {self.quantity}'"


item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item("Samsung", 300, 2)
item2.pay_rate = 0.5  # self.pay_rate
item2.apply_discount()
print(item2.price)

print(Item.all)
# for instance in Item.all:
#     print(instance.name)

# item1 = Item("Phone", 100, 5)
# item2 = Item("Laptop", 1000, 4)
#
# print(Item.__dict__) # All the attributes for class level
# print(item1.__dict__) # All the attributes for instance level
# print(item2.__dict__)

# print(item1.calculator_total_price())
# print(item2.calculator_total_price())

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
#
# print(item2.name)
# print(item2.price)
# print(item2.quantity)
