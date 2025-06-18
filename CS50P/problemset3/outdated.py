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
        if d >= 1 and d <= 31:
            
