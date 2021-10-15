from item import Item

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

item1.apply_increment(0.3)
item1.apply_discount()

print(item1.price)
