import subprocess
import helper

CustomKeyBindings = {}
ExistingKeyBindings = {}

def GetAllSystemKeybinds():
		
	Dconf_functions = list()
	
	Dconf_functions.append("activate-window-menu")
	Dconf_functions.append("begin-move")
	Dconf_functions.append("begin-resize")
	Dconf_functions.append("close")
	Dconf_functions.append("cycle-group")
	Dconf_functions.append("cycle-group-backward")
	Dconf_functions.append("cycle-panels")
	Dconf_functions.append("cycle-panels-backward")
	Dconf_functions.append("cycle-windows")
	Dconf_functions.append("cycle-windows-backward")
	Dconf_functions.append("lower")
	Dconf_functions.append("maximize")
	Dconf_functions.append("maximize-horizontally")
	Dconf_functions.append("maximize-vertically")
	Dconf_functions.append("move-to-workspace-down")
	Dconf_functions.append("move-to-workspace-left")
	Dconf_functions.append("move-to-workspace-right")
	Dconf_functions.append("move-to-workspace-up")
	Dconf_functions.append("move-to-workspace-last")
	Dconf_functions.append("panel-main-menu")
	Dconf_functions.append("panel-run-dialog")
	Dconf_functions.append("show-desktop")
	Dconf_functions.append("switch-applications")
	Dconf_functions.append("switch-applications-backward")
	Dconf_functions.append("switch-group")
	Dconf_functions.append("switch-group-backward")
	Dconf_functions.append("switch-input-source")
	Dconf_functions.append("switch-input-source-backward")
	Dconf_functions.append("switch-panels")
	Dconf_functions.append("switch-panels-backward")
	Dconf_functions.append("switch-to-workspace-1")
	Dconf_functions.append("switch-to-workspace-2")
	Dconf_functions.append("switch-to-workspace-3")
	Dconf_functions.append("switch-to-workspace-4")
	Dconf_functions.append("switch-to-workspace-5")
	Dconf_functions.append("switch-to-workspace-6")
	Dconf_functions.append("switch-to-workspace-7")
	Dconf_functions.append("switch-to-workspace-8")
	Dconf_functions.append("switch-to-workspace-9")
	Dconf_functions.append("switch-to-workspace-10")
	Dconf_functions.append("switch-to-workspace-11")
	Dconf_functions.append("switch-to-workspace-12")
	Dconf_functions.append("switch-to-workspace-down")
	Dconf_functions.append("switch-to-workspace-last")
	Dconf_functions.append("switch-to-workspace-left")
	Dconf_functions.append("switch-to-workspace-right")
	Dconf_functions.append("switch-to-workspace-up")
	Dconf_functions.append("switch-windows")
	Dconf_functions.append("switch-windows-backward")
	Dconf_functions.append("toggle-maximized")
	Dconf_functions.append("toggle-shaded")
	Dconf_functions.append("unmaximize")
	

	for func in Dconf_functions:
		shortcut = (subprocess.check_output(["gsettings", "get", "org.gnome.desktop.wm.keybindings", func])).rstrip()
		keyBindObj = helper.Keybind(helper.keyString_to_keyCode(shortcut))
		ExistingKeyBindings[keyBindObj] = func


def GetAllCustomKeybinds():
	with open("user-set_Keybinds.txt") as f:
		lines = f.readlines()

	for line in lines:
		customKeybind = line.split(':')
		shortcut = customKeybind[0]
		command = customKeybind[1].rstrip()
		
		keyBindObj = helper.Keybind(helper.keyString_to_keyCode(shortcut))
		CustomKeyBindings[keyBindObj] = command
		





		
		
		
