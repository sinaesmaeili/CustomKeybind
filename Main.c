#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	printf("##---Custom Keybind Application---##\n");
	
	int funcID;
	char cmd[255] = "gsettings get org.gnome.desktop.wm.keybindings ";
	
	printf("Which function would you like to view?\n");
	printf("(1) close window\n");
	printf("(2) maximize window\n");
	printf("(3) activate window menu\n");

	scanf("%d", &funcID);

	switch (funcID){
		case 1:
			strcat(cmd, "close");
			break;
		case 2:
			strcat(cmd, "maximize");
			break;
		case 3:
			strcat(cmd, "activate-window-menu");

	}
	
	system(cmd);

	return 0;
}
