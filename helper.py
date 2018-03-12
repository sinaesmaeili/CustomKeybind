from pynput import keyboard

def convertToKeyCode(rawKeys):

	keyCodeList = list()
	for key in rawKeys:
		if key == "Ctrl":
			keyCodeList.append(keyboard.Key.ctrl)
		elif key == "Alt":
			keyCodeList.append(keyboard.Key.alt)
		elif key == "Super":
			keyCodeList.append(keyboard.Key.cmd)
		elif key == "F1" or key == "f1":
			keyCodeList.append(keyboard.Key.f1)
		elif key == "F2" or key == "f2":
			keyCodeList.append(keyboard.Key.f2)
		elif key == "F3" or key == "f3":
			keyCodeList.append(keyboard.Key.f3)
		elif key == "F4" or key == "f4":
			keyCodeList.append(keyboard.Key.f4)
		elif key == "F5" or key == "f5":
			keyCodeList.append(keyboard.Key.f5)
		elif key == "F6" or key == "f6":
			keyCodeList.append(keyboard.Key.f6)
		elif key == "F7" or key == "f7":
			keyCodeList.append(keyboard.Key.f7)
		elif key == "F8" or key == "f8":
			keyCodeList.append(keyboard.Key.f8)
		elif key == "F9" or key == "f9":
			keyCodeList.append(keyboard.Key.f9)
		elif key == "F10" or key == "f10":
			keyCodeList.append(keyboard.Key.f10)
		elif key == "F11" or key == "f11":
			keyCodeList.append(keyboard.Key.f11)
		elif key == "F12" or key == "f12":
			keyCodeList.append(keyboard.Key.f12)
		else:
			keyCodeList.append(keyboard.KeyCode.from_char(key))
	
	return keyCodeList

