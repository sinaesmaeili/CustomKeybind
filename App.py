from pynput import keyboard
from pynput.keyboard import Controller
import os
from Tkinter import *
import thread
import helper

current = set() 
currentKeys = list()
cmd = ""
keysID = 0

CustomKeyBindings = {}

# Controller for outputting text with keyboard
controller = Controller()

def listen_to_keyboard(string, delay):
		def on_press(key):
			# Checking if current key combination exists in COMBINATION structure
			for i in CustomKeyBindings:
				if key in i.keyList:
					current.add(key)
					if all(k in current for k in i.keyList):
						os.system("gnome-terminal -e 'bash -c \"" + CustomKeyBindings[i]  + "; exec bash\"'")
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

		clearButton = Button(self, text = "Clear", command = self.clear_event)
		clearButton.place(x=550, y=350)
		
		commandLabel = Label(self, text = "Command: ")
		commandLabel.place(x=350, y=150)
		
		instructionLabel = Label(self, text = "Seperate keys with '-'")
		instructionLabel.place(x=350, y=250)

		self.errorLabel = Label(self)
		self.errorLabel.place(x=500, y=325)
		
		self.commandEntry = Entry(self)
		self.commandEntry.place(x=430, y=150)
		
		self.hotkeyEntry = Entry(self)
		self.hotkeyEntry.place(x=500, y=300)
		
	def ctrl_event(self):
		if "Ctrl" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Ctrl-")
		
	def alt_event(self):
		if "Alt" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Alt-")
		
	def super_event(self):
		if "Super" not in self.hotkeyEntry.get():
			self.hotkeyEntry.insert('end',"Super-")
		
	def apply_event(self):
		global cmd
		self.errorLabel.config(text = "")#Clear error message if any

		cmd = self.commandEntry.get()
		if cmd == "":
			self.errorLabel.config(text = "Error, no command given")
		
		
		rawHotKeys = self.hotkeyEntry.get().split("-")
		
		currentKeys = helper.convertToKeyCode(rawHotKeys, self.errorLabel)[:]	
		
		#If no errors present, proceed 
		if(self.errorLabel["text"] == ""):
			keybindObj = Keybind(currentKeys)
			CustomKeyBindings[keybindObj] = cmd
			del currentKeys[:]
		
		self.commandEntry.delete(0, 'end')
		self.hotkeyEntry.delete(0, 'end')

	def clear_event(self):
		self.hotkeyEntry.delete(0, 'end')		
		self.errorLabel.config(text = "")
		
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

for x in CustomKeyBindings:
	print str(x.ID) + '---->' + CustomKeyBindings[x]
	for key in x.keyList:
		print str(key)




