# Collect password / test length

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

input = input("Please enter your password: ")

if len(input) < 6:
    print ("Your password " + Fore.WHITE + Back.WHITE + Style.BRIGHT + str(input) + Fore.WHITE+ Back.BLACK + Style.BRIGHT + " is" + Fore.RED+ Back.BLACK + Style.BRIGHT + " too short.")
    print("Please enter a password with at least" + Fore.RED + Style.BRIGHT + " 6 characters.")