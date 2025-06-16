def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dnodsign = d.replace("$","")
    return float(dnodsign)

def percent_to_float(p):
    pnopsign = p.replace("%","")
    d_converted = float(pnopsign) / 100
    return d_converted


main()
