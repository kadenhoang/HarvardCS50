def main():
    while True:
        try:
            fraction = input("Fraction:" )
            percentage = convert(fraction)
            print(gauge(percentage))
            break

        except (ValueError,ZeroDivisionError):
            pass

def convert(fraction):
    numer, deno = fraction.split("/")
    numer = int(numer)
    deno = int(deno)
    if numer > deno:
        raise ValueError
    return round((numer/deno)*100)



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
