import re

name = input("Name?:").strip()
matches = re.search(r"^(.+), (.+)$",name)
#using matches.groups() will return the values in ()
# if matches:
#     last,first = matches.groups()
# or:
#     first = matches.group(2)
#     last = matches.group(1)

# name = f"{first}{last}"

# or:
name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
