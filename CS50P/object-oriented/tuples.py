def main():
    student = get_student()
    print(f"{name} from {house})

def get_student():
    name = input("Name:")
    house = input("House:")
    # tuples use ()
    # the data inside cannot be changed (immuatable)
    return (name, house)

if __name__ == "__main__":
    main
