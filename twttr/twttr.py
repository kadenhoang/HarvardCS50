# ask the user for input
tweet = input("Input: ").lower().strip()

print("Output: ", end="")
# loop through every letter to find the match
for letter in tweet:
# if the letter is not in the list
    if not letter in ["a","e","i","o","u"]:
# print the letter without create a new line
        print(letter,end="")

print()

