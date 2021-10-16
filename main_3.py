from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)
# print("---------------------")
# for item in Item.all:
#     print(item)

item1 = Item("My Phone", 750)

# # Setting  an Attribute
# item1.name = "Other name"  # len  = 10
#
# # Getting  an Attribute
# print(item1.name)

# item1.apply_increment(0.3)
# item1.apply_discount()
# print(item1.price)

item1.send_email()

item2 = Phone("Nokia", 840, 3)
item2.apply_discount()
print(item2.price)