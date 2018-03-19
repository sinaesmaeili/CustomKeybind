from pynput import keyboard


class Keybind:
	def __init__(self,keys):	
		self.keyList = tuple(keys[:]);
		
	def __hash__(self):
		return hash(self.keyList)
		
	def __eq__(self, other):
		return self.keyList == other.keyList
		
	def __ne__(self, other):
		return not(self == other)

def convertToKeyCode(rawKeys, errMsg = None):
	keyCodeList = list()
	for key in rawKeys:
		if key == "Ctrl" or key == "Control":
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
		elif key == "Shift":
			keyCodeList.append(keyboard.Key.shift)
		elif key == "Escape":
			keyCodeList.append(keyboard.Key.esc)
		elif key == "Down":
			keyCodeList.append(keyboard.Key.down)
		elif key == "Left":
			keyCodeList.append(keyboard.Key.left)
		elif key == "Right":
			keyCodeList.append(keyboard.Key.right)
		elif key == "Up":
			keyCodeList.append(keyboard.Key.up)
		elif key == "Tab":
			keyCodeList.append(keyboard.Key.tab)
		elif key == "space":
			keyCodeList.append(keyboard.Key.space)
		elif key == "Home":
			keyCodeList.append(keyboard.Key.home)
		elif key == "End":
			keyCodeList.append(keyboard.Key.end)
		elif len(key) > 1:
			if errMsg: 
				errMsg.config(text = "Error, invalid key: " + key)
		else:#Single letter/number key, ex: 'a'
			if keyboard.KeyCode.from_char(key) not in keyCodeList:
				keyCodeList.append(keyboard.KeyCode.from_char(key.lower()))
			elif errMsg:
				errMsg.config(text = "Error, duplicate key: " + key)
	
	return keyCodeList

def keyString_to_keyCode(rawKeys):
	keyCodeList = list()	
	tempStr = rawKeys.replace("[", "")
	tempStr = tempStr.replace("]", "")
	tempStr = tempStr.replace("'", "")
	tempStr = tempStr.replace("<", "")
	splitkeys = tempStr.split(",")
	splitKeys = splitkeys[0].split(">")
		
	keyCodeList = convertToKeyCode(splitKeys)
	
	return keyCodeList

def keyList_to_keyString(rawKeys):
	keyString = "['"
	
	for key in rawKeys:

		#If not last item
		if key != rawKeys[-1]:
			keyString += ("<" + key + ">")
		else:
			keyString += (key + "']")	
	
	return keyString		


