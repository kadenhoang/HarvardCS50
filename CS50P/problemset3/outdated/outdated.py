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
    date = input("Date:").strip()
    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= day <= 31 and 1 <= month <= 12:
            break
    except:
        try:
            old_m, old_d, year = date.split(" ")
            old_d = old_d.replace(",", "")
            day = int(old_d)
            year = int(year)
            for i in range(len(monthslist)):
                if old_m == monthslist[i]:
                    month = i + 1
                    break
            if 1 <= day <= 31:
                break
        except:
            pass

print(f"{year}-{month:02}-{day:02}")
