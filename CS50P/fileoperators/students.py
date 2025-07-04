# create a list to store the student info
students = []

with open("students.csv") as file:
    #loop through all the student in the file
    for name in file:
        #seperate the info by a comma
        name,province = name.rstrip().split(",")
        #append the splited info in students
        #it can be row[0] and row[1] if name is not assigned to "name" n "province"
        students.append(f"{name} is in {province}")

#sorted use to sort the date in order
for student in sorted(students):
    print(student)


