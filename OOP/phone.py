from item import Item


class Phone(Item):


    def __init__(self, name: str, price: float, quantity=0, broken_phones =0):

        #Call to super functions to have access to all attributes /methods
        super().__init__(
            name,price,quantity
        )


        assert broken_phones >=0, f"Broken_phones {broken_phones} is not or greater equal to zero"




        self.broken_phones = broken_phones