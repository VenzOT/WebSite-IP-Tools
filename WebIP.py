import socket #line:1
import ssl #line:2
from colorama import Fore ,init #line:3
import os #line:4
import platform #line:5
import os #line:6
import json #line:7
import traceback #line:8
import datetime #line:9
import requests #line:10
import psutil #line:11
from colorama import Fore ,Style #line:12
from urllib .request import Request ,urlopen #line:13
from pystyle import *#line:14
import random #line:15
import string #line:16
import base64 #line:17
from cryptography .fernet import Fernet #line:18
import sys ,re ,time ,os .path ,subprocess ,threading ,ctypes ,shutil #line:19
from time import sleep #line:20
import csv #line:21
import hashlib #line:22
import fade #line:23
w =Fore .LIGHTRED_EX #line:26
b =Fore .BLACK #line:27
g =Fore .LIGHTGREEN_EX #line:28
y =Fore .LIGHTYELLOW_EX #line:29
m =Fore .RED #line:30
c =Fore .LIGHTCYAN_EX #line:31
lr =Fore .LIGHTRED_EX #line:32
lb =Fore .WHITE #line:33
os .system ("WebIP by Venz")#line:34
sayuri ='''
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
'''#line:47
System .Size (120 ,30 )#line:48
System .Clear ()#line:49
Anime .Fade (Center .Center (sayuri ),Colors .black_to_white ,Colorate .Vertical ,interval =0.1 ,enter =True )#line:50
init ()#line:52
def clear_screen ():#line:54
    ""#line:55
    if platform .system ()=="Windows":#line:56
        os .system ("cls")#line:57
    else :#line:58
        os .system ("clear")#line:59
def get_ip_and_port (OO0O0OOOOOO0OOOOO ):#line:61
    try :#line:62
        OOO0O000OOO0O0O00 =socket .gethostbyname (OO0O0OOOOOO0OOOOO )#line:63
        print (f"L'adresse IP de {OO0O0OOOOOO0OOOOO} est {OOO0O000OOO0O0O00}")#line:64
        O0O0OOOO0000O0OO0 =ssl .create_default_context ()#line:66
        with O0O0OOOO0000O0OO0 .wrap_socket (socket .socket (socket .AF_INET ),server_hostname =OO0O0OOOOOO0OOOOO )as O000000OO0O00OOO0 :#line:68
            O000000OO0O00OOO0 .connect ((OO0O0OOOOOO0OOOOO ,443 ))#line:69
            print (f"{OO0O0OOOOOO0OOOOO} utilise HTTPS sur le port 443")#line:70
            return OOO0O000OOO0O0O00 ,443 #line:71
    except ssl .SSLError :#line:72
        print (f"{OO0O0OOOOOO0OOOOO} utilise HTTP sur le port 80")#line:73
        return OOO0O000OOO0O0O00 ,80 #line:74
    except Exception as O00O0OO0O0O00O0O0 :#line:75
        print (f"Erreur lors de la vérification : {O00O0OO0O0O00O0O0}")#line:76
        return None ,None #line:77
def afficher_menu ():#line:79
    print (Fore .GREEN +""" 
  _  __     
 ██▒   █▓▓█████  ███▄    █ ▒███████▒
▓██░   █▒▓█   ▀  ██ ▀█   █ ▒ ▒ ▒ ▄▀░
 ▓██  █▒░▒███   ▓██  ▀█ ██▒░ ▒ ▄▀▒░ 
  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒  ▄▀▒   ░
   ▒▀█░  ░▒████▒▒██░   ▓██░▒███████▒
   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒
   ░ ░░   ░ ░  ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒  
     ░░     ░      ░   ░ ░ ░ ░ ░ ░
      ░     ░  ░         ░   ░ ░    
     ░                     ░   by venz.db""")#line:91
    print (Fore .CYAN    +"╔═══       Tools         ═══╗ ╔═══     My Socials      ═══╗ ╔═══     More Tools    ═══╗")#line:92
    print (Fore .CYAN    +"║  {1} WebSite Ip & Port    ║ ║  {Discord} venz.db        ║ ║  {Github}               ║")#line:93
    print (Fore .CYAN    +"║  {2} Exit                 ║ ║  {Github} VenzOT          ║ ║                         ║")#line:94
    print (Fore .CYAN    +"║  {Hx Shop}  .gg/HxShop    ║ ║  {TikTok} .venzot         ║ ║                         ║")#line:95
    print (Fore .CYAN    +"║  {HxH Serv} .gg/hxh       ║ ║  {Serv Commu} .gg/commufr ║ ║                         ║")#line:96
    print (Fore .CYAN    +"╚═══                     ═══╝ ╚═══                     ═══╝ ╚═══                   ═══╝")#line:97
def main ():#line:99
    while True :#line:100
        clear_screen ()#line:101
        afficher_menu ()#line:102
        OO0O00OO0O0O0OOO0 =input ("Sélectionnez une option: ")#line:103
        if OO0O00OO0O0O0OOO0 =="1":#line:105
            OOO0OOO000O000OOO =input ("Entrez le nom du site web (e.g., www.example.com): ")#line:106
            print ("")#line:107
            O000O0O0000O000O0 ,OO0000O0O00OO00OO =get_ip_and_port (OOO0OOO000O000OOO )#line:108
            if O000O0O0000O000O0 :#line:109
                input ("Appuyez sur Entrée pour continuer...")#line:111
        elif OO0O00OO0O0O0OOO0 =="2":#line:112
            print ("Au revoir !")#line:113
            break #line:114
        else :#line:115
            input ("Option invalide. Appuyez sur Entrée pour essayer à nouveau...")#line:116
if __name__ =="__main__":#line:118
    main ()#line:119
