

#Parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details ")
        print("")
        print("Name " , self.name)
        print("Age ", self.age)
        print("Gender", self.gender)


#Johan = User("Johan", 21, "Male")
#Johan.show_details()


#Child class

class Bank(User):

    def __init__(self,name,age,gender,):
        super().__init__(
            name,age,gender
        )
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)

#johan = Bank("Johan",20,"Male")

# johan.deposit(100)
# johan.deposit(400)


    def withdraw(self,amount):
        self.amount =amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : ", self.balance)
        else:
            self.balance = self.balance-self.amount
            print("Account balance has been updated : $ ", self.balance)
#
# johan = Bank("Johan",20,"Male")
# johan.deposit(200)
# johan.withdraw(5)
# johan.withdraw(500)


    def view_balance(self):
        self.show_details()
        print("Account balance has been updated  :$" ,self.balance)


johan = Bank("Johan", 20, "Male")

johan.view_balance()