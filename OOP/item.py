import csv


class Item:

    #class atribute
    pay_rate = 0.8 #payrate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):


        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if len(value) >10:
            raise Exception("The name is too long")
        self.__name = value



    def calculate_total_price(self):
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )


    @staticmethod
    def is_integer(num):
        # we will count out the floats are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False




    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"
