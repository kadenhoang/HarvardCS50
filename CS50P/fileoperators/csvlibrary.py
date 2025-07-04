import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, province in reader:
        students.append({"name":name,"province":province})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['province']}")
