def main():
    print(get_fraction())


# create a loop if user input is not a fraction
def get_fraction():
    while True:
        try:
            # ask user for the fraction

            fraction = input("Fraction:" )

            #declare the parts of the fraction
            numer, deno = fraction.split("/")
            numer = int(numer)
            deno = int(deno)

            #return out the percentage
            return round((numer/deno)*100)
            break

        # if it is not a fraction then use exception
        except (ValueError,ZeroDivisionError):
            pass

