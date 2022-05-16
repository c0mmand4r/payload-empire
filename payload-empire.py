import os
from sys import platform
from functions import windows, linux, android, ios, banner

try:
    import colorama
    import pyfiglet
except:
    os.system("pip install colorama && pip install pyfiglet")
from colorama import Fore
import pyfiglet

if platform == 'win32':
    print(Fore.RED + "[!] The script is written only for Linux")
    exit()

try:
    os.system("msfvenom")

except:
    print(Fore.RED + "[!] Install metasploit for use this script")    


def clear():
    os.system('clear')
clear()

banner.banner()

choice = input(f"{Fore.GREEN}[+] Enter your choice:: ")

if choice == '1':
    clear()
    windows.win()

if choice == '2':
    clear()
    linux.lin()

if choice == '3':
    clear()
    android.andr()

if choice == '4':
    clear()
    ios.ios()

if choice == '99':
    clear()
    Fore.RESET
    exit()