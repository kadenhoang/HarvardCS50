import sys
import os
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

for arg in sys.argv[1:]:
    if not arg.lower().endswith((".jpg",".jpeg",".png")):
        print("Invalid input")
        sys.exit(1)

#split and only assign the extention
inputext = os.path.splitext(sys.argv[1])[1].lower()
outputext = os.path.splitext(sys.argv[2])[1].lower()

if inputext != outputext:
    print("Input and output have different extensions")
    sys.exit(1)

# make a shirt file
shirt = Image.open("shirt.png")
#make after.jpg file using arg
image = Image.open(sys.argv[1])

#get the size of the shirt file
shirtsize = shirt.size
# make the image fit the size of the shirt file
fit = ImageOps.fit(image,shirtsize)
#paste it in the image
fit.paste(shirt,shirt)
#save into a new file using arg
fit.save(sys.argv[2])

