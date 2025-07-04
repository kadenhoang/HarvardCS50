students = []

with open("students.csv") as file:
    for line in file:
        name, province = line.rstrip().split(",")
        student = {"name" : name, "province": province}
        students.append(student)

def get_province(student):
    return student["province"]

# key= (use to sort what variable you want, in this case, sort by province)
# key=lambda student: student["name"] (anonymous function wt no name) if you dont wanna create a function
for student in sorted(students, key=get_house)
    print(f"{student['name']} is in {student['province']})
