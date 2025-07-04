name = input("what's your name? ")

#use "open" to open a file
# first arg is to name the file. seconds is what u wanna do
#"w" = write, "a" = appends, if not "a" the file only save 1 name very time it runs
#with - as file = open and close after the indented line is done
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# or
#file = open("names.txt", "a")
#file.write()
#file.close()



