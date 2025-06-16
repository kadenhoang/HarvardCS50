def main():
    # ask user for the time
    answer = input("What time is it?: ")
    # call the function
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("Breakfast time")
    if time >= 12 and time <= 13:
        print("Lunch time")
    if time >= 18 and time <= 19:
        print("Dinner time")


def convert(time):
    # split the string in to two, seperate by ":"
    # python automatically assign it to hours, minutes
    hours, minutes = time.split(":")
    newmins = float(minutes) / 60
    return float(hours) + newmins


if __name__ == "__main__":
    main()
