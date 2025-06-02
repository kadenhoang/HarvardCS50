#define a function or create a class
def getGuess():
    guess = int(input("make a guess: "))
    return guess

#define the main()
def main():
    guess = getGuess()
#put " : " after if - the next line should space inward
#means the next line is within the if function
    if guess == 10:
        print("correct")
    else:
        print("try again")

# make this line so the function works
main()
