months = [
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
    try:
        date = intput("Date:")
        m,d,y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if (d >= 1 and d <= 31) and (m >= 1 and m <= 12):
            break

    except:
        try:
            old_m,old_d,old_y = date.split("")

