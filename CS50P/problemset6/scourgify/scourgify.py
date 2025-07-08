import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

students = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)


with open(sys.argv[2],"w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first","last","house"])

    for student in students:
        last, first = student["name"].split(",")
        house = student["house"]
        writer.writerow({"first":first,"last":last,"house":house})
