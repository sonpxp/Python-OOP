import csv


class Item:
    # can set default = 0 ex: quality = 0
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quality {quantity} is not greater than or equal to zero!"

        # assert to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-only Attribute
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate  # Item.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-only Attribute
    def name(self):
        # print("You are trying to get name") ...
        return self.__name

    @name.setter
    def name(self, value):
        # print("You are trying to set name")
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value

    def calculator_total_price(self):
        return self.__price * self.quantity

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
