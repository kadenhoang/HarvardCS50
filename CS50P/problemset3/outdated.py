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

        m,d,y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if (d >= 1 and d <= 31) and (m >= 1 and m <= 12):
            break

    except:
        try:
            old_m,old_d,y = date.split(" ")
            old_m = int(old_m)
            old_d = int(old_d)
            for i in range(len(m)):
                if old_m == m[i]
                    m = i + 1
            d = old_d.replace(",","")

        except:
            pass

print(f"{y}-{m:02}-{d:02}")

