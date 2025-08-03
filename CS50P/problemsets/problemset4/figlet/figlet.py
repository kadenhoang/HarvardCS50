from pyfiglet import Figlet
from random import choice
from sys import argv

figlet = Figlet()

# two command-line arguments zero or two
if len(argv) == 1:
    randomfont = True
elif len(argv) == 3 and (argv[1] != "-f" or argv[1] != "--font"):
    randomfont = False
else:
    sys.exit(1)

# ask user for input
text = input("Input:").strip().lower()


if randomfont == False:
    try:
        figlet.setFont(font=argv[2])
        print(figlet.renderText(text))
    except:
        print("Invalid Font")
        sys.exit(1)
else:
    font = choice(figlet.getFonts())


#outputs the text in the desired font
print("Output: ", figlet.renderText(text))

