import os

def loadModel(model, world):													##MODEL is a PATH. WORLD is a dictionary. CHDIR needs to be set before calling function
	offset = len(world)
	localmodel = open(model,"r")
	numberoflines = sum(1 for line in open(model,"r"))+1
	#print(numberoflines)
	for i in range(1,numberoflines):											##Get the number of lines in the model file
		curline = str(localmodel.readlines(i)).strip().replace("\\n","").replace("[","").replace("]","").replace("'","").split(",")
		#print(curline)
		#input("^Curline")
		world["vert{}".format(i+offset)] = [float(curline[0]),float(curline[1]),float(curline[2])]		##APPEND vertices to world, read from file
	return world

def printWorld(world):															##prints all vertices all organized and delicious
	for i in range(1,len(world)+1):
		print("vert{}:".format(i) ,world["vert{}".format(i)])
	return 0
	


#DEBUG ZONE, LOADMODEL AND PRINTWORLD. UNCOMMENT THE FOLLOWING IN ORDER TO ACCESS:
"""
input("ENTERING DEBUG AREA\n")
world = dict()																	##declare world as dictionary
os.chdir("C:\\Users\\Batarda\\Desktop\\Python-Screwery\\TerminalGraphicsModule")			##chdir to model location
world = loadModel("Model.txt", world)
printWorld(world)
input("CLOSING DEBUG\n")
"""