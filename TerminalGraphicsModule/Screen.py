import os

def printScreen(screen):
	os.system("cls")
	for i in range(0,(len(screen)*2)+1):
		print("=",end="")
	for i in range(0,len(screen)):
		print("")
		for h in range (0,len(screen[0])):
			print("" ,screen[i][h] , end="")
	print("")
	for i in range(0,(len(screen)*2)+1):
		print("=",end="")
	print("")
	return 0

def makeScreen(x,y):
	screen = []
	for i in range (0,y):
		screen.append(["■"]*x)
	return screen
	
def start():
	##Using relative paths in order to open the versioninfo.txt file
	dirPath = os.path.dirname(os.path.abspath(__file__))
	os.chdir(dirPath)
	
	print((open("VersionInfo.txt","r").read()), "\n")
	choice = int(input("""Select Resolution:
	1. 15x15
	2. 25x20
	3. 25x25
	4. 40x25 \n"""))
	if (choice == 1):
		x = y = 15
	elif (choice == 2):
		x = 25
		y = 20
	elif (choice == 3):
		x = y = 25
	elif (choice == 4):
		x = 40
		y = 25
	else:
		print("Are you serial? Defaulting to 20x20")
		input("...")
		x = y = 20
	screen = makeScreen(x,y)
	return screen