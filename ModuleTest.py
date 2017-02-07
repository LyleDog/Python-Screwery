import os
from TerminalGraphicsModule import Screen
from TerminalGraphicsModule import Render
from TerminalGraphicsModule import World

##Obtaining the path of the script
dirPath = os.path.dirname(os.path.abspath(__file__))

screen = Screen.start()
Screen.printScreen(screen)
input("Cleared?\n")
os.system("cls")
input("Starting World and Render tests...\n")
world = {}
##applying dirpath to chdir
os.chdir(dirPath)

world = World.loadModel("TerminalGraphicsModule\\Model.txt", world)
World.printWorld(world)
input("Cleared?\n")
os.system("cls")
input("Starting Raytrace tests...\n")
clippingplane = []
clippingplane = Render.createClippingplane(float(input("Width of clipping plane?\n")),screen,float(input("Clipping plane distance?\n")))
print("clippingplane =", clippingplane)
input("Cleared?\n")
os.system("cls")
world = Render.chooseVertices(world,clippingplane)
projection = {}
projection = Render.createProjection(world,clippingplane)
World.printWorld(projection)
input("Cleared?\n")
projectedtoscreen = Render.ProjectiontoScreen(projection,screen,clippingplane)