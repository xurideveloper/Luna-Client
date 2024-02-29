import os
from colorama import Style, Back, Fore

# Luna @ Interface Module

def Send(Sign, Message, Client='Luna'):
    if Sign == 'Success':
        return print(Fore.BLUE + '@' + Client + ', ' + Fore.GREEN + Message)

    if Sign == 'Issue':
        return print(Fore.BLUE + '@' + Client + ', ' + Fore.RED + Message)

    if Sign == 'Warn':
        return print(Fore.BLUE + '@' + Client + ', ' + Fore.YELLOW + Message)

    if Sign == 'Default':
        return print(Fore.BLUE + '@' + Client + ', ' + Fore.WHITE + Message)

def Input(Message, Client='Luna'):
    return input(Fore.BLUE + '@' + Client + ', ' + Fore.WHITE + Message)