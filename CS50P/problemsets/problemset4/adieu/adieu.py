import inflect

p = inflect.engine()

#create a list that holds names
names = []
# loop forever
while True:
    # prompts the user for names
    try:
        name = input("Name:").strip().title()
        names.append(name)
    except EOFError:
        print()
        break

#bid adieu to the names using join()
print("Adieu, adieu, to",p.join(names))
