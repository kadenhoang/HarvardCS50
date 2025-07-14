import re

email = input("what is your email?:").strip()

# . = any character except a newline
# * = 0 or more repetitions in character
# + = 1 or more repetitions in character
# ? = 0 or 1 repetitions
# {m} = m repetitions
# {m,n} = m to n repetiions
# ^ = match the begining of the string(str start with what comes after ^)
# & = match the end of the string(str ends after $)
# [] = set of characters [a-zA-Z0-9_] = only allow this set of alphanumeric
# [^] = any characters except smt. ex:[^@] = anything except @
# \w = [a-zA-Z0-9_] = aplphanumeric (more friendly)
# r(raw) = treat the string as written. if \n = newline then r"\n" = output the "n"
if re.search(r"^[^@]+@[^@]+\.edu$", email):
        # (r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email)
        # (r"^\w+@\w+\.edu$", email)
        # (r"^(\w\.)@(\w\.)?\w+\.edu$",email,re.IGNORECASE)
    print("Valid")
else:
    print("Invalid")
