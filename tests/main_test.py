#!/usr/bin/env python3

import gtts
import pygame
import speech_recognition as sr

from gtts import gTTS

# Verifica la compatibilidad del dispositivo de audio
r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Ajustando el volumen...")

        # Ajusta el volumen para que sea compatible con el dispositivo de audio
        r.adjust_for_ambient_noise(source)
        
        # Escucha y reconoce la voz
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)

        except sr.UnknownValueError:
            print("No se pudo entender el texto.")

except sr.RequestError as e:
    print(f"Error: {e}")


