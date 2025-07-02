def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False

    i=0

    if s[i].isdigit():
        if s[i] == "0":
            return False
        elif not s[i:].isdigit():
            return False
        else:
            return True
    return True


if __name__ == "__main__":
    main()
