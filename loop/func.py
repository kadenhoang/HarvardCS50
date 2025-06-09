def main():
    numbers = get_num()
    meow(numbers)

def get_num():
    # while True means always true
    while True:
        n = int(input("How many Meow?: "))
        if n > 0:
            break
    return n

# create a fuction meow with paremeter(n)
# (n) is the name that I need for the function to calculate
def meow(n):
    for _ in range(n):
        print("Meow")

main()
