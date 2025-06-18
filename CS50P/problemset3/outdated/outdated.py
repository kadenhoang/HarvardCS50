monthslist = [
     "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]


while True:
    #ask the user for input
    date = input("Date:").strip().title()
    try:
        #split the date input in to 3 part
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        #check if the date and month is within correct range
        if 1 <= day <= 31 and 1 <= month <= 12:
            break
    except:
        try:
            # split the original input again with " "
            old_m, old_d, year = date.split(" ")
            old_d = old_d.replace(",", "")
            day = int(old_d)
            year = int(year)

            # if the month match with the indice of the list
            for i in range(len(monthslist)):
                if old_m == monthslist[i]:
                    month = i + 1
                    break
            if 1 <= day <= 31:
                break
        except:
                pass

print(f"{year}-{month:02}-{day:02}")
