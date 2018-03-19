from pynput import keyboard
from pynput.keyboard import Controller
import os
import subprocess
from Tkinter import *
import thread
import helper
import KeybindDB
current = set() 
currentKeys = list()
cmd = ""

#Initialize dictionary containing all current supported ubuntu keybinds
KeybindDB.GetAllSystemKeybinds()

#Get all previously set custom keybinds
KeybindDB.GetAllCustomKeybinds()

# Controller for outputting text with keyboard
controller = Controller()

def listen_to_keyboard(string, delay):
	def on_press(key):
		# Checking if current key combination exists in COMBINATION structure
		for i in KeybindDB.CustomKeyBindings:
			if key in i.keyList:
				current.add(key)
				if all(k in current for k in i.keyList):
					print  KeybindDB.CustomKeyBindings[i] 
					os.system("gnome-terminal -e 'bash -c \"" + KeybindDB.CustomKeyBindings[i]  + "; exec bash\"'")
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


class Window(Frame):	
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Custom Keybindings")
		
		self.pack(fill=BOTH, expand=1)
		
		ctrlButton = Button(self, text = "Ctrl", command = self.ctrl_event)
		ctrlButton.place(x=5, y=285)
		
		altButton = Button(self, text = "Alt", command = self.alt_event)
		altButton.place(x=150, y=285)
		
		superButton = Button(self, text = "Super", command = self.super_event)
		superButton.place(x=75, y=285)	
		
		shiftButton = Button(self, text = "Shift", command = self.shift_event)
		shiftButton.place(x=150, y=250)		
		
		escapeButton = Button(self, text = "Escape", command = self.escape_event)
		escapeButton.place(x=5, y=250)	
		
		tabButton = Button(self, text = "Tab", command = self.tab_event)
		tabButton.place(x=82, y=250)	
		
		spaceButton = Button(self, text = "Space", command = self.space_event)
		spaceButton.place(x=5, y=215)	
		
		homeButton = Button(self, text = "Home", command = self.home_event)
		homeButton.place(x=75, y=215)	
		
		endButton = Button(self, text = "End", command = self.end_event)
		endButton.place(x=150, y=215)	
		
		upButton = Button(self, text = "Up", command = self.up_event)
		upButton.place(x=62, y=320)	
		
		downButton = Button(self, text = "Down", command = self.down_event)
		downButton.place(x=50, y=350)	
		
		leftButton = Button(self, text = "Left", command = self.left_event)
		leftButton.place(x=5, y=350)	
		
		rightButton = Button(self, text = "Right", command = self.right_event)
		rightButton.place(x=111, y=350)	
		
		applyButton = Button(self, text = "Apply", command = self.apply_event)
		applyButton.place(x=300, y=350)

		clearButton = Button(self, text = "Clear", command = self.clear_event)
		clearButton.place(x=400, y=350)
		
		clearAllButton = Button(self, text = "Clear All Custom Keybinds", command = self.clearAll_event)
		clearAllButton.place(x=500, y=350)
		
		commandLabel = Label(self, text = "Command: ")
		commandLabel.place(x=300, y=150)
		
		instructionLabel = Label(self, text = "Seperate keys with '-'")
		instructionLabel.place(x=300, y=250)
		
		keyBankLabel = Label(self, text = "Standard Keys")
		keyBankLabel.place(x=50,y=175)

		hotKeyLabel = Label(self, text = "---->")
		hotKeyLabel.place(x=250, y=300)		
		
		self.errorLabel = Label(self)
		self.errorLabel.place(x=500, y=325)
		
		self.commandEntry = Entry(self)
		self.commandEntry.place(x=380, y=150)
		
		self.hotkeyEntry = Entry(self)
		self.hotkeyEntry.place(x=300, y=300)
				
		
	def ctrl_event(self):
		if "Ctrl" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Ctrl-")
		
	def alt_event(self):
		if "Alt" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Alt-")
		
	def super_event(self):
		if "Super" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Super-")
			
	def shift_event(self):
		if "Shift" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Shift-")
			
	def escape_event(self):
		if "Escape" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Escape-")
			
	def tab_event(self):
		if "Tab" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Tab-")
			
	def space_event(self):
		if "Space" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"space-")
			
	def home_event(self):
		if "Home" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Home-")
			
	def end_event(self):
		if "End" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"End-")
			
	def up_event(self):
		if "Up" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Up-")
			
	def down_event(self):
		if "Down" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Down-")
			
	def left_event(self):
		if "Left" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Left-")
			
	def right_event(self):
		if "Right" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Right-")
		
	def apply_event(self):
		global cmd
		self.errorLabel.config(text = "")#Clear error message if any

		cmd = self.commandEntry.get()
		if cmd == "":
			self.errorLabel.config(text = "Error, no command given")
		
		
		rawHotKeys = self.hotkeyEntry.get().split("-")
		
		currentKeys = helper.convertToKeyCode(rawHotKeys, self.errorLabel)[:]	
		
		keybindObj = helper.Keybind(currentKeys)

		if keybindObj in KeybindDB.CustomKeyBindings:
			self.errorLabel.config(text = "Error, keybind already exists")
		elif keybindObj in KeybindDB.ExistingKeyBindings:
			self.errorLabel.config(text = "Error, keybind already exists")
		
		#If no errors present, proceed 
		if(self.errorLabel["text"] == ""):
			KeybindDB.CustomKeyBindings[keybindObj] = cmd
			
			keyBindsFile = open("user-set_Keybinds.txt", "a")
			stringtoWrite = helper.keyList_to_keyString(rawHotKeys) + ":" + cmd + "\n"
			keyBindsFile.write(stringtoWrite)
			keyBindsFile.close()
			
			del currentKeys[:]

		
		self.commandEntry.delete(0, 'end')
		self.hotkeyEntry.delete(0, 'end')

	def clear_event(self):
		self.hotkeyEntry.delete(0, 'end')		
		self.errorLabel.config(text = "")
		
	def clearAll_event(self):
		KeybindDB.CustomKeyBindings.clear()
		f = open("user-set_Keybinds.txt", "w")
		f.close()
		
root = Tk();
root.geometry("800x400")

app = Window(root)
thread.start_new_thread(listen_to_keyboard, ('thread', 1))

root.protocol('WM_DELETE_WINDOW', root.iconify)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()

for x in KeybindDB.CustomKeyBindings:
	for key in x.keyList:
		print str(key)





