from pyfiglet import Figlet
import sys
import random

# Prompt user for input
text = input("Input: ")
# Give the Figlet function a variable
figlet = Figlet()
# Get list of fonts under pyfiglet
font_list = figlet.getFonts()
# Program actions if user types 3 CLAs
if (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and (sys.argv[2] in font_list)
):
        chosen_font = figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
# Program actions if user types 1 CLA
elif len(sys.argv) == 1:
        random_font = figlet.setFont(font=random.choice(font_list))
        print(figlet.renderText(text))
else:
    sys.exit("Invalid Usage")
