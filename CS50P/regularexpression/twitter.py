import re

url = input("URL: ").strip()

#replace(smt need to be replace, smt I use to replace the original)
# username = url.replace("https://twitter.com/", "")

#or

# removeprefix do not need a second argument
# username = url.removeprefix("https://twitter.com/")

#or

#subtitude(pattern to replace, replace with?, where to put it)
#? 0 or 1 repetition ("s" or (input) can be there or not)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

#or
matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

print(f"Username:", matches.group(3))



