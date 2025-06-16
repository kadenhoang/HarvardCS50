def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # plate cannot be less than two or more than 6 leters
    if len(s) < 2 or len(s) > 6:
        return False
    # fist two letters cannot be numbers
    if not s[0:2].isalpha():
        return False
    # plate cannot be anything else than al and num
    if not s.isalnum():
        return False

    i=0
    #or
    #for i in range(len(s)):
        # first number cannot be 0
    if s[i].isdigit():
        if s[i] == "0":
            return False
        # after first digit found, the next letters can only be digit
        elif not s[i:].isdigit():
            return False
        else:
            return True
    return True


main()
