# varialbe to keep track
amount_due = 50

# create a loop for the amount_due is >0
while amount_due > 0:
    print("Amount Due:", amount_due)
    # ask the user to insert coin
    coin = int(input("Insert Coin:"))
    # check if correct coin
    if coin in [25,10,5]:
        amount_due -= coin

change_owed = abs(amount_due)

print("Change Owed:", change_owed)


