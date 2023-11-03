
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def logo():
    print(Bcolors.FAIL + '=' * 40)
    print(Bcolors.FAIL + '  ___   _   ___    ___ _  _____ \t\t developer: RitenMaer')
    print(Bcolors.FAIL + ' | _ ) /_\ |   \  | _ ) ||_   _|\t\t author_of_idea: RomanFox69')
    print(Bcolors.FAIL + ' | _ \/ _ \| |) | | _ \ |__| |  \t\t source: https://github.com/mrRiten/BadBLT.git')
    print(Bcolors.FAIL + ' |___/_/ \_\___/  |___/____|_|  \t\t for jokes and fune')
    print(Bcolors.FAIL + '=' * 40)
