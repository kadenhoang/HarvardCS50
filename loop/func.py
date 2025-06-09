def main()
    numbers = get_num()
    meow(numbers)

def get_num():
    while True:
        n = int(input("How many Meow?: "))
            if n > 0:
                break
    return n

def meow(n):
    for _ in range(n)
        print("Meow")
