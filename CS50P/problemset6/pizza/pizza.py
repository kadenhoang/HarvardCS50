from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    print("Too few command-line arguments")
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    print("not a CSV file")
    sys.exit(1)

table = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

except FileNotFoundError:
    print("file does not exist")
    sys.exit(1)

print(tabulate(table, headers = "keys", tablefmt="grid"))
