def main():
    userinput = get_int("Enter an int: ")


def get_int(prompt):
    #create a loop to ask for int if input is not int
    while True:
    # ask user for input
        try:
            # use int(input())
            # or assign with prompt and get it from the main
            userinput = int(input(prompt))

        # if the input is not an integer, make an exeption
        except ValueError:
            print("That is not an integer")
        # after checking, if int = true then breakout of the loop
        else:
            break
print("the integer is:", userinput)









