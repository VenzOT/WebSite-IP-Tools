import socket
import ssl
from colorama import Fore, init
import os
import platform
import os
import json
import traceback
import datetime
import requests
import psutil
from colorama import Fore, Style
from urllib.request import Request, urlopen
from pystyle import *
import random
import string
import base64
from cryptography.fernet import Fernet
import sys, re, time, os.path, subprocess, threading, ctypes, shutil
from time import sleep
import csv
import hashlib
import fade


w = Fore.LIGHTRED_EX
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.RED
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.WHITE
os.system("WebIP by Venz")

sayuri = '''
 ██▒   █▓▓█████  ███▄    █ ▒███████▒
▓██░   █▒▓█   ▀  ██ ▀█   █ ▒ ▒ ▒ ▄▀░
 ▓██  █▒░▒███   ▓██  ▀█ ██▒░ ▒ ▄▀▒░ 
  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒  ▄▀▒   ░
   ▒▀█░  ░▒████▒▒██░   ▓██░▒███████▒
   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒
   ░ ░░   ░ ░  ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒  
     ░░     ░      ░   ░ ░ ░ ░ ░ ░
      ░     ░  ░         ░   ░ ░    
     ░                     ░        
'''
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(sayuri), Colors.black_to_white, Colorate.Vertical, interval=0.1, enter=True)

init()

def clear_screen():
    """Efface l'écran du terminal."""
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

def get_ip_and_port(site):
    try:
        ip_address = socket.gethostbyname(site)
        print(f"L'adresse IP de {site} est {ip_address}")

        context = ssl.create_default_context()

        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=site) as s:
            s.connect((site, 443))
            print(f"{site} utilise HTTPS sur le port 443")
            return ip_address, 443
    except ssl.SSLError:
        print(f"{site} utilise HTTP sur le port 80")
        return ip_address, 80
    except Exception as e:
        print(f"Erreur lors de la vérification : {e}")
        return None, None

def afficher_menu():
    print(Fore.RED    + """ 
  _  __     
 █     █░▓█████  ▄▄▄▄       ██▓ ██▓███  
▓█░ █ ░█░▓█   ▀ ▓█████▄    ▓██▒▓██░  ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▒██▒▓██░ ██▓▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ░██░▒██▄█▓▒ ▒
░░██▒██▓ ░▒████▒░▓█  ▀█▓   ░██░▒██▒ ░  ░
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ░▓  ▒▓▒░ ░  ░  by venz.db
  ▒ ░ ░   ░ ░  ░▒░▒   ░     ▒ ░░▒ ░     
  ░   ░     ░    ░    ░     ▒ ░░░       
    ░       ░  ░ ░          ░           
                      ░                 """)
    print(Fore.CYAN    + "╔═══       Tools         ═══╗ ╔═══     My Socials      ═══╗ ╔═══     More Tools     ═══╗")
    print(Fore.CYAN    + "║  {1} WebSite Ip & Port    ║ ║  {Discord} venz.db        ║ ║  {Github}                ║")
    print(Fore.CYAN    + "║  {2} Exit                 ║ ║  {Github} VenzOT          ║ ║https://github.com/VenzOT/║")
    print(Fore.CYAN    + "║  {Hx Shop}  .gg/HxShop    ║ ║  {TikTok} .venzot         ║ ║                          ║")
    print(Fore.CYAN    + "║  {HxH Serv} .gg/hxh       ║ ║  {Serv Commu} .gg/commufr ║ ║                          ║")
    print(Fore.CYAN    + "╚═══                     ═══╝ ╚═══                     ═══╝ ╚═══                    ═══╝")

def main():
    while True:
        clear_screen()  
        afficher_menu()
        choix = input("Sélectionnez une option: ")

        if choix == "1":
            site = input("Entrez le nom du site web (e.g., www.example.com): ")
            print("")
            ip_address, port = get_ip_and_port(site)
            if ip_address:
                
                input("Appuyez sur Entrée pour continuer...")
        elif choix == "2":
            print("Au revoir !")
            break
        else:
            input("Option invalide. Appuyez sur Entrée pour essayer à nouveau...")

if __name__ == "__main__":
    main()
