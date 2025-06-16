#use [] to create a list
#then use {} to create a dictionaries
#=> create a list of dictionaries


students = [
    {"Name":"Vu", "Country":"Vietnam", "Sign":"Leo"},
     {"Name":"Hero", "Country":"Tanzania", "Sign":"Scorpion"},
     {"Name":"Peter", "Country":"America", "Sign": None}
]

for student in students:
    print(student["Name"], student["Country"], student["Sign"],sep=", ")
