
# ask user for input, assign it to camelcase
camelcase = input("camelCase: ")
#print camelcase without newline (end="") and without space (sep="")
print(camelcase, end="")

for letter in camelcase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

