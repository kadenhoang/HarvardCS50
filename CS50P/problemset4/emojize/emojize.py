import emoji

# ask user for a string
str = input("Input: ").strip()
# emojize the string
emojized = emoji.emojize(str)
#output the emoji
print("Output:",emojized)
