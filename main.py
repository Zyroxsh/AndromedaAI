#!/usr/bin/env python3

##########################################################
#
#                   Script by @zyrox
#          Think healthy, be healty, hack healty
#                       vß 2.1.7
#
##########################################################


import os
import src
import sys
import time
import gtts
import random
import requests
import pywhatkit as kit
import subprocess as sp
import functions as func
import speech_recognition as sr

from gtts import gTTS
from random import choice
from datetime import datetime
from termcolor import colored
from src import random_sentences
from functions import artificial_inteligence


import logging
print([logging.getLogger(name) for name in logging.root.manager.loggerDict])


# Necesary variables
listener = sr.Recognizer()

# Extrayendo datos de .env
USERNAME = 'Zyrox'
BOTNAME = 'Andromeda'


def answer(text):
    """De texto a voz"""
    tts = gTTS(text, lang='es')
    tts.save('./audio/output.mp3')

    os.system('mpv --speed=1.500 ./audio/output.mp3 > /dev/null 2>&1')
    os.remove('./audio/output.mp3')


def userGreet():
    """Saluda al usuario conforme a la hora local"""
    
    global hour
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        answer(f"Buenos dias {USERNAME}")

    elif hour >= 12 and hour < 20:
        answer(f"Buenas tardes {USERNAME}")

    elif hour >= 20 and hour < 6:
        answer(f"Buenas noches {USERNAME}")


if __name__ == "__main__":
    try:
        sp.run('clear', shell=True)
        print(colored("\n\n[+] Aplicacion inicializada y en escucha...\n", 'green'))
        userGreet()

        # Entrada del usuario
        while True:
            with sr.Microphone() as micro:
                listener.adjust_for_ambient_noise(micro)    # Eliminando sonido ambiente
                voice = listener.listen(micro)

                try:
                    global rec
                    global query
                    rec = listener.recognize_google(voice, language='es-ES')
                    query = str(rec)

                
                    print(colored("# ", 'red') + query)
                    print(colored("> ", 'green') + choice(src.random_sentences.on_it_text))
                    answer(choice(src.random_sentences.on_it_text))


                    if 'abre una terminal' in query or 'abreme una terminal' in query or 'abre una kitty' in query or 'abreme una kitty' in query:
                        print(colored("[+] ", 'green') + "Abriendo Kitty Terminal...")
                        answer("Abriendo terminal")
                        sp.run('/usr/bin/kitty | sleep 2 & disown', shell=True)

                    if 'abre burpsuit' in query or 'abreme burpsuit' in query or 'abre el proxy' in query or 'abreme el proxy' in query:
                        print(colored("[+] ", 'green') + "Abriendo BurpSuite Proxy...")
                        answer("Abriendo BurpSuite Proxy")
                        sp.run('/usr/bin/burpsuite | sleep 5 & disown', shell=True)

                    if 'cuenta un chiste' in query or 'cuéntame un chiste' in query or 'cuenta una broma' in query or 'cuéntame una broma' in query:
                        print(colored("> ", 'green') + "Voy a pensarla")
                        answer("Voy a pensarlo")
                        headers = {
                                'Accept': 'application/json'
                                }
                        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
                        print(colored("> ", 'green') + "Ya la tengo. Aunque esta en inglés, pero no pasa nada")
                        answer("Ya la tengo. Aunque esta en inglés, pero no pasa nada")
                        print(colored('> ', 'green') + res["joke"])
                        
                        tts = gTTS(res["joke"], lang='en')
                        tts.save('./audio/output.mp3')

                        os.system('mpv --speed=1.500 ./audio/output.mp3 > /dev/null 2>&1')
                        os.remove('./audio/output.mp3')


                    if 'busca en internet' in query or 'busca en google' in query or 'busca en gugel' in query or 'busca en googel' in query:
                        
                        if 'internet' in query:
                            lista = query.split()
                            indice = lista.index('internet')
                            sublista1 = lista[indice:]
                            sublista2 = sublista1[1:]
                            search = ' '.join(sublista2)
                            kit.search(search)

                        elif 'google' in query:
                            lista = query.split()
                            indice = lista.index('google')
                            sublista1 = lista[indice:]
                            sublista2 = sublista1[1:]
                            search = ' '.join(sublista2)
                            kit.search(search)


                    if 'actualiza el sistema' in query:
                        sysname = sp.check_output("lsb_release -a | grep --color=never 'Parrot' | awk '{print $2,$3,$4,$5}'", shell=True)
                        sysname = sysname.decode('utf-8').strip('\n')
                        sp.run('clear', shell=True)
                        print(colored("> ", 'green') + "Buscando actualizaciones para " + colored(sysname, 'red'))
                        answer(f"Buscando actualizaciones para {sysname}. Introduce la contraseña de root")
                        sp.run('sudo apt update', shell=True)
                        print(colored("> ", 'green') + "Instalando actualizaciones")
                        answer("Instalando actualizaciones")
                        sp.run('sudo parrot-upgrade', shell=True)
                        print(colored("> ", 'green') + "Sistema actualizado")
                        answer("Sistema actualizado")
                        

                    if 'apaga el equipo' in query or 'apaga el sistema' in query or 'apaga el ordenador' in query:
                        answer("¿Seguro que quieres apagar el sistema?")
                        apagar = input(colored("[!] ", 'yellow') + "¿Seguro que quieres apagar el sistema? [Y/n] " + colored('# ', 'red'))

                        if apagar == "Y":
                            sysname = sp.check_output("lsb_release -a | grep --color=never 'Parrot' | awk '{print $2,$3,$4,$5}'", shell=True)
                            sysname = sysname.decode('utf-8').strip('\n')
                            answer("De acuerdo Zyrox, apagando sistema operativo" + sysname)
                            print(colored("[!] Apagando sistema", 'yellow'))
                            sp.run("poweroff", shell=True)

                        else:
                            print(colored("> ", 'green') + "¡Sabía que no me dejarias! Bien hecho " + USERNAME)
                            answer("¡Sabia que no me dejarias! Bien hecho " + USERNAME)


                    if 'activa la IA' in query or 'activa la inteligencia artificial' in query or 'enciende la IA' in query or 'enciende la inteligencia artificial' in query:
                        print(colored("[+] ", 'green') + "Activando asistente de Inteligencia Artificial...")
                        answer("Activando asistente de Inteligencia Artificial")
                        artificial_inteligence.main()


                    # Despedida del usuario
                    if 'apágate' in  query or 'desconéctate' in query or 'apagate' in query or 'desconectate' in query:      # Comprobar si el usuario quiere salir
                        # Dependiendo de la hora decir algo o no
                        if hour >= 21 and hour < 6:
                            print(colored("> ", 'green') + "Buenas noches señor, que descanse.")
                            answer("Buenas noches señor, que descanse.")

                            print(colored("\n\n[!] Saliendo...\n", 'yellow'))
                            break
                            sys.exit()

                        else:
                            answer(choice(src.random_sentences.good_bye_text))

                            print(colored("\n\n[!] Saliendo...\n", 'yellow'))
                            break
                            sys.exit()


                except sr.UnknownValueError as e:
                    print(colored("# ", 'red') + "???")
                    print(colored("> ", 'green') + "Lo siento señor, no le he entendido.")
                    answer("Lo siento señor, no le he entendido.")


    # Error handling
    except KeyboardInterrupt:
        print(colored("\n\n[!] Saliendo...\n", 'red'))
        sys.exit(1)

    except sr.RequestError as e:
        print(colored(f"\n\n[FATAL - RequestError] Un error inesperado ha sucedido --> {e}\n", 'red'))
        sys.exit(1)

    except OSError as e:
        print(colored(f"\n\n[FATAL - OSError] Un error inesperado ha sucedido --> {e}\n", 'red'))
        sys.exit(1)

    #except Exception as e:
    #    print(colored(f"\n\n[FATAL - Exception] Un error inesperado ha sucedido --> {e}\n", 'red'))
    #    sys.exit(1)


