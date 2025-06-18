m = [
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
    date = input("Date:")
    try:
        month_num, day, year = date.split("/")
        month_num = int(month_num)
        day = int(day)
        year = int(year)
        if 1 <= day <= 31 and 1 <= month_num <= 12:
            break
    except:
        try:
            old_m, old_d, year = date.split(" ")
            old_d = old_d.replace(",", "")
            day = int(old_d)
            year = int(year)
            for i in range(len(m)):
                if old_m == m[i]:
                    month_num = i + 1
                    break
            if 1 <= day <= 31:
                break
        except:
            pass

print(f"{year}-{month_num:02}-{day:02}")
