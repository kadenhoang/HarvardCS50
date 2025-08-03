import validators

email = validators.email(input("email?"))

if email:
    print("Valid")
else:
    print("Invalid")
