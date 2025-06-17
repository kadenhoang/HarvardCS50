#create a list of dishes:
itemlist = {"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}

#create a loop to continue the order until done
while True:
    try:
    # ask user to make order
        item = input("Item:")

        if item == itemlist:
            print(item, itemlist[item])
        else:
            print()
    except EOFEerror:
        pass


#
