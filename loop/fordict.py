# {} = dictionary , it allow us to associate one thing to another using ":"
#  think of a dictionary, the first word is the keyword, the second is the definition
# in this case, Vu is the keyword and Vietnam is what we want to know.

studentsdict = {"Vu":"Vietnam", "Hashita":"India", "Hero":"Tanzania", "Jordan":"Malay",}

for student in studentsdict:
    #using student only print the keyword, for definition whe need [indice "student"]
    print(student, studentsdict[student],sep=", ")
