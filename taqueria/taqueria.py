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

total = 0.0
#create a loop to continue the order until done
while True:
    try:
    # ask user to make order
        order = input("Item:").title()

        if order == itemlist:
            total += itemlist[order]
            print(f"total: ${total:2f}")
        else:
            pass

    except EOFError:
        pass


#
