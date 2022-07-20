import csv


class Item:

    #class atribute
    pay_rate = 0.8 #payrate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


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
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"    #Paren    #Parentclass



class Phone(Item):

    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones =0):

        #Call to super functions to have access to all attributes /methods
        super().__init__(
            name,price,quantity
        )

        #assert price >= 0, f"Price {price} is not greater than zero!"
        #assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        assert broken_phones >=0, f"Broken_phones {broken_phones} is not or greater equal to zero"



        #self.name = name
        #self.price = price
        #self.quantity = quantity
        self.broken_phones = broken_phones

        Phone.all.append(self)


phone1 = Phone("jscPhonev10", 500, 5,1)

print(phone1.calculate_total_price())

#phone1.broken_phones = 1  is removed as the attritubue is given in the object phone

phone2 = Phone("jscPhonev20", 700, 5,1)

#phone2.broken_phone = 1


print(Item.all)
print(Phone.all)






