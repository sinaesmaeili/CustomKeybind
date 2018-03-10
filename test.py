from pynput import keyboard
from subprocess import call
import os
from Tkinter import *
 
keybind = ""
cmd = ""

CustomKeyBindings = {}

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
		
		self.commandEntry = Entry(self)
		self.commandEntry.place(x=430, y=150)
		
		self.hotkeyEntry = Entry(self)
		self.hotkeyEntry.place(x=500, y=300)

	def ctrl_event(self):
		self.hotkeyEntry.insert('end',"Ctrl");
		
	def alt_event(self):
		self.hotkeyEntry.insert('end',"Alt");
		
	def super_event(self):
		self.hotkeyEntry.insert('end',"Super");
		
	def apply_event(self):
		global cmd
		cmd = self.commandEntry.get()
		keybind = self.hotkeyEntry.get()
		
		self.commandEntry.delete(0, 'end')
		self.hotkeyEntry.delete(0, 'end')		
		
		CustomKeyBindings[keybind] = cmd;
		
		keybind = ""
	
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
	print x + '---->' + CustomKeyBindings[x]




