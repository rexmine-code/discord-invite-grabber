import requests
import json
import os
import time
import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)
assi = """
    ██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  discord : https://discord.gg/MJ27DYPm82
    ██║██╔██╗ ██║██║   ██║██║   ██║   █████╗      ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
    ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗       by rexmine2
    ██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║           v1.0
    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def grab():
    print(Fore.RED+assi)
    id = input("Enter the server id: ")

    response = requests.get(f"https://discord.com/api/guilds/{id}/widget.json")
    data = response.json()
    invite = data.get('instant_invite')
    name = data.get('name')
    if invite:
        print(Back.GREEN+f"Server name: {Back.RESET+name}")
        print(Back.GREEN+f"grabed invite: {Back.RESET+invite}")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        grab()
    else:
        print(Back.RED+"grab failed")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        grab()
def grabwordlist():
    wordlist = input("Enter the wordlist path: ")
    with open(wordlist, "r") as file:
        lines = file.readlines()
        for line in lines:
            id = line.strip()
            response = requests.get(f"https://discord.com/api/guilds/{id}/widget.json")
            data = response.json()
            invite = data.get('instant_invite')
            name = data.get('name')
            if invite:
                print(Back.GREEN+f"Server name: {Back.RESET+name}")
                print(Back.GREEN+f"grabed invite: {Back.RESET+invite}")
            else:
                print(Back.RED+"grab failed")
def main():
    print(Fore.RED+assi)
    print(Fore.GREEN+"1. Grab invite")
    print(Fore.GREEN+"2. Grab invite from wordlist")
    print(Fore.GREEN+"3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        grab()
    elif choice == "2":
        grabwordlist()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        main()

main()