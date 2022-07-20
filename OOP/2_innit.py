

class Item:

    #class atribute
    pay_rate = 0.8 #payrate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):   #init method will be performed for every object beinng initialised from the same class
        #Run validations to the received arguments
        assert price  >= 0 , f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"



        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity



    def calculate_total_price(self):
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone",100,5)



item2 = Item("Laptop",1000,3)


item1.apply_discount()

print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)





#print(Item.__dict__)  #magic method for all the attributes in class level
#print(item1.__dict__) #bzw for instance level

#print(item2.calculate_total_price())