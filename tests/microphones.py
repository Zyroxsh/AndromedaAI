import speech_recognition as sr

listener = sr.Recognizer()

m = None

for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
    if microphone_name == "Microphone (Realtek Audio)":
        m = sr.Microphone(device_index=i)