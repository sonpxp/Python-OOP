import csv

"""
class Item:
    # can set default = 0 ex: quality = 0
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quality {quantity} is not greater than or equal to zero!"

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}, {self.price}, {self.quantity}'"


# Item.instantiate_from_csv()
# print()
# print(Item.all)

# print(Item.is_integer(5.9))


class Phone(Item):
    # all = []

    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        # Call to super function to have access to attribute / method
        super().__init__(name, price, quantity)

        # run validations to the received arguments
        assert broken_phones >= 0, f"broken hones {broken_phones} is not greater than or equal to zero!"

        # assert to self object
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)


phone1 = Phone("IPhone11", 500, 3, 1)
# print(phone1.calculator_total_price())
# phone2 = Phone("IPhone12", 700, 5, 1)

print(Item.all)
# print(Phone.all)

"""
