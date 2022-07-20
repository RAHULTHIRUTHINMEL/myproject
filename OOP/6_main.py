#this is used to instantiate instances for files 7,8



from item import Item

from phone import Phone


# Item.instantiate_from_csv()
#
# print(Item.all)

item1 = Item("MyItem", 750)


#Setting an attribute
item1.name = "OtherItem"

#Setting an attribute
print(item1.name)

