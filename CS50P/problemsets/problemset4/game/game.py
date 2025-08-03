import random

# prompts user for a level

while True:
        # if it is not a positive number, prompt again
    try:
        level = int(input("Level: "))
        if level > 0:
            break

    except ValueError:
        pass

#randomly generates an ineger between 1 and n
random_number = random.randint(1,level)



while True:
        # prompts the user for a integer
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too Small!")
            elif guess > random_number:
                print("Too Large!")
            else:
                print("Just right!")
                break
        # not a positive number, prompt again
    except ValueError:
        pass







