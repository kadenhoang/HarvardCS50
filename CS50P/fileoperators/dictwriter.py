import csv

name = input("Name?:")
province = input("From?:")

with open("students2.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","province"])
    writer.writerow({"name": name, "province": province})

#use dictwiter so that I know exact which column contain which info
#I only have to type which info comes first (Name,Province)
