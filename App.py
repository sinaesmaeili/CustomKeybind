from pynput import keyboard
from subprocess import call
import os
from Tkinter import *
 
currentKeys = list()
cmd = ""
keysID = 0

CustomKeyBindings = {}

#Need to make a keybind object so it can be used as a dictionary key
#Regular lists arent hashable 
class Keybind:
	def __init__(self,keys):
		global keysID
		self.ID = keysID
		keysID += 1	
		self.keyList = keys[:];
		
	def __hash__(self):
		return hash((self.ID))
		
	def __eq__(self, other):
		return self.ID == other.ID
		
	def __ne__(self, other):
		return not(self == other)
	

class Window(Frame):	
	
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Custom Keybindings")
		
		self.pack(fill=BOTH, expand=1)
		
		ctrlButton = Button(self, text = "Ctrl", command = self.ctrl_event)
		ctrlButton.place(x=200, y=300)
		
		altButton = Button(self, text = "Alt", command = self.alt_event)
		altButton.place(x=300, y=300)
		
		superButton = Button(self, text = "Super", command = self.super_event)
		superButton.place(x=400, y=300)
		
		applyButton = Button(self, text = "Apply", command = self.apply_event)
		applyButton.place(x=400, y=350)
		
		commandLabel = Label(self, text = "Command: ")
		commandLabel.place(x=350, y=150)
		
		instructionLabel = Label(self, text = "Seperate keys with '-'")
		instructionLabel.place(x=350, y=250)
		
		self.commandEntry = Entry(self)
		self.commandEntry.place(x=430, y=150)
		
		self.hotkeyEntry = Entry(self)
		self.hotkeyEntry.place(x=500, y=300)
		
	def ctrl_event(self):
		self.hotkeyEntry.insert('end',"Ctrl-")
		
	def alt_event(self):
		self.hotkeyEntry.insert('end',"Alt-")
		
	def super_event(self):
		self.hotkeyEntry.insert('end',"Super-")
		
	def apply_event(self):
		global cmd
		cmd = self.commandEntry.get()
		
		rawHotKeys = self.hotkeyEntry.get().split("-")
		
		for key in rawHotKeys:
			if key == "Ctrl":
				currentKeys.append(keyboard.Key.ctrl)
			elif key == "Alt":
				currentKeys.append(keyboard.Key.alt)
			elif key == "Super":
				currentKeys.append(keyboard.Key.cmd)
			else:
				currentKeys.append(keyboard.KeyCode.from_char(key))
		
		
		keybindObj = Keybind(currentKeys)
		CustomKeyBindings[keybindObj] = cmd
		del currentKeys[:]
		
		self.commandEntry.delete(0, 'end')
		self.hotkeyEntry.delete(0, 'end')		
		
				
		
	
root = Tk();
root.geometry("800x400")

app = Window(root)

root.protocol('WM_DELETE_WINDOW', root.iconify)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()

for x in CustomKeyBindings:
	print str(x.ID) + '---->' + CustomKeyBindings[x]
	for key in x.keyList:
		print str(key)




