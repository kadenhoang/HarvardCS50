import sys

for arg in sys.argv:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

linecount = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            linecount += 1
        print(linecount)
except FileNotFoundError:
    print("File does not found")

