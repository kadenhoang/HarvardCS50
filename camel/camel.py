camelcase = input("camelCase: ")
print (camelcase.end="".sep="")

for letter in camelcase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        

