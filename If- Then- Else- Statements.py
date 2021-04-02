# Collect password / test length

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# input function will promt user to enter a string and store the value in the variable input
input = input("Please enter your password: " + Fore.WHITE + Back.WHITE + Style.BRIGHT + "")

# using if-then line, test to see if the length of the string is less thasn 6 characters
# if true the following lines are executed
if len(input) < 6:
    print (Fore.WHITE+ Back.BLACK + Style.BRIGHT + "Your password " + Fore.WHITE + Back.WHITE + Style.BRIGHT + str(input) + Fore.WHITE+ Back.BLACK + Style.BRIGHT + " is" + Fore.RED+ Back.BLACK + Style.BRIGHT + " too short.")
    print("Please enter a password with at least" + Fore.RED + Style.BRIGHT + " 6 characters.")
# if not the lines are skipped
