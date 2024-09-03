import os

def open_kitty():
    os.system('kitty | sleep 2 & disown')
