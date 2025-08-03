students = [
    {"name" : "Vu", "house": "Gryffindor"},
    {"name": "Phuc", "house": "Slytherin"},
    {"name": "An", "house": "Gryffindor"},
    {"name": "Trung", "house": "Ravenclaw"}
]

#Set() class use add, while list[] use append to add data in a variable.
#create a object "houses" to store the methods of class set() to use it method.
houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
