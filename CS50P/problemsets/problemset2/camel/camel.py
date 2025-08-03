
# ask user for input, assign it to camelcase
camelcase = input("camelCase: ")
#print snakecase without newline (end="")
#print("snake_case: ", end="")

for letter in camelcase:
    # if the letter is uppercase [isupper()] then:
    if letter.isupper():
        print("snake_case:","_" + letter.lower(), end="")
    else:
        print(letter, end="")
print()  # Print a newline at the end

