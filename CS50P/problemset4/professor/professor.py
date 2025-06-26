import random


def main():
    score = 0
    level = get_level()

# generate 10 problems base on level
    for _ in range(10):
        x , y = generate_integer(level)
        correct = x + y

# let user answer 3 times
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} ="))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {correct}")

# print out the score
    print("Score:",score)




#prompt the user for a level 1,2 or 3
def get_level():
    while True:
        try:
            n = int(input("Level:"))
            if 0 < n < 4:
                return n

        except ValueError:
            pass

#randomly generate numbers base on level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10,99), random.randint(10,99)
    else:
        return random.randint(100,999), random.randint(100,999)

if __name__ == "__main__":
    main()
