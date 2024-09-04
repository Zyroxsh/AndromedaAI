#!/usr/bin/env python3


import langchain_core
import langchain_ollama

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


# Global variables
model = OllamaLLM(model="dolphin-llama3")


def main():

    result = model.invoke(input="Hola como estas")
    print(result)



if __name__ == "__main__":
    main()


