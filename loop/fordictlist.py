#use [] to create a list
#then use {} to create a dictionaries
#=> create a list of dictionaries


students = [
    {"Vu":"Vietnam", "Sign":"Leo"},
     {"Hero":"Tanzania","Sign":"Scorpion"},
     {"Peter":"America","Sign": None}
]

for student in range(len(students)):
    print(student, students[student])
