def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name:")
    house = input("House:")
    # tuples use ()
    # the data inside cannot be changed (immuatable)
    return (name, house)

if __name__ == "__main__":
    main()
