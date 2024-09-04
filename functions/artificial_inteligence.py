#!/usr/bin/env python3


import os
import gtts
import termcolor
import langchain_core
import langchain_ollama

from gtts import gTTS
from termcolor import colored
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


# Global variables
model = OllamaLLM(model="dolphin-llama3")



def answer(text):
    """De texto a voz"""
    tts = gTTS(text, lang="es")
    tts.save('./audio/output.mp3')

    os.system('mpv --speed=1.500 ./audio/output.mp3 > /dev/null 2>&1')
    os.remove('./audio/output.mp3')


def ask(user_input):

    result = model.invoke(input=user_input)
    print(colored("> ", 'green') + result)
    answer(result)


def main(query):

    ask(query)




if __name__ == "__main__":
    
    main(query)


