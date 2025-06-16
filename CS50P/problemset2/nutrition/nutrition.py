# ask the user to item
fruit = input("Item: ").strip().lower()

#create a dictionary of fruit
fruitdict = {
    "apple":"130",
    "avocado":"50",
    "banana":"110",
    "cantaloup":"50"
}

# if the item is in the dict then print calories
if fruit in fruitdict:
    print("Calories:", fruitdict[fruit])
# or else, ignore
else:
    print(end="")
