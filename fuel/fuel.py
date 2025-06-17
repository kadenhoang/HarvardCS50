def main():
    fraction = input("Fraction: ")
    print(get_fraction(fraction))


# create a loop if user input is not a fraction
def get_fraction(fraction):
    while True:
        try:
            # ask user for the fraction

            #fraction = input("Fraction:" )

            #declare the parts of the fraction
            numer, deno = fraction.split("/")
            numer = int(numer)
            deno = int(deno)

            #print out the percentage
            print(round(numer/deno)*100)
            break

        # if it is not a fraction then use exception
        except (ValueError,ZeroDivisionError):
            pass

