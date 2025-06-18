def main():
    #fraction = input("Fraction:" )
    print(get_fraction(),"%",sep="")




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


        # if it is not a fraction then use exception
        except (ValueError,ZeroDivisionError):
            pass

        else:
            break
main()
