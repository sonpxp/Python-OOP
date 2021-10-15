from item import Item


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

# print(Item.all)
# print(Phone.all)
