from pynput import keyboard
from subprocess import call
import os

# The key combination to check
# Uses python map (key, value) data structure called dictionary
COMBINATION = dict([('firefox', {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('b')}),
					('chromium-browser', {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('a')})])

# The currently active modifiers
current = set()


def on_press(key):
	# Checking if current key combination exists in COMBINATION structure
	for index, value in COMBINATION.iteritems():
	    if key in value:
	        current.add(key)
	        if all(k in current for k in value):
	        	call([index])
	    if key == keyboard.Key.esc:
	        listener.stop()

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

# Initializing keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()