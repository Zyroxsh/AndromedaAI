import pyttsx3

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id)

# 0 = English
# 1 = Español

tts.say("Hola! esto es una simple prueba de voz en español. ¡Escuchame subnormal!")
tts.runAndWait()