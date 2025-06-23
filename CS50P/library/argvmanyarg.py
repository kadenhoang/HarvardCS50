from sys import argv

if len(argv) < 2:
    print("Too Few Argument")

# arg loop through argv starting from indice 1
for arg in argv[1:]:
    print("Hello,", arg)

