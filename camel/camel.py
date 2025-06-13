
# ask user for input, assign it to camelcase
camelcase = input("camelCase: ")
#print snakecase without newline (end="")
print("snake_case: ", end="")

for letter in camelcase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

