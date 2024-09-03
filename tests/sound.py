#!/usr/bin/env python3

import os
import gtts
from gtts import gTTS


print('Generando...')
tts = gTTS('¡Hola!, soy Andromeda, tu asistente virtual con inteligencia artificial integrada. ¿Como puedo ayudarte en este hermoso dia?', lang='es')
tts.save('example.mp3')

print('Reproduciendo...')
os.system('mpv --speed=1.500 example.mp3 > /dev/null 2>&1')


