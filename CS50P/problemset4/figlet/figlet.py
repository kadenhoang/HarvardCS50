from pyfiglet import Figlet
from random import choice
from sys import argv

fidlet = Figlet()

# two command-line arguments zero or two
if len(argv) == 1:
    randomfont = True
elif len(argv) == 3 and (argv[1] != "-f" or argv[1] != "--font"):
    randomfont = False
else:
    sys.exit(1)
# ask user for input
text = input("Input:").strip().lower()

# get a list ot fonts
figlet.getFonts()

if randomfont = True:
    font = 


#outputs the text in the desired font


