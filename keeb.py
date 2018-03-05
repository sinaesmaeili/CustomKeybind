from pynput import keyboard

# The key combination to check
COMBINATION = [{keyboard.Key.ctrl, keyboard.KeyCode.from_char('s')},
			   {keyboard.Key.ctrl, keyboard.KeyCode.from_char('a')}]

# The currently active modifiers
current = set()


def on_press(key):
	for i in COMBINATION:
	    if key in i:
	        current.add(key)
	        if all(k in current for k in i):
	            print('All modifiers active!')
	    if key == keyboard.Key.esc:
	        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()