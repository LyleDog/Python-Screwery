import os
from TerminalGraphicsModule import Screen
from TerminalGraphicsModule import Render
from TerminalGraphicsModule import World

screen = Screen.start()
Screen.printScreen(screen)
input("Cleared?\n")
os.system("cls")
input("Starting World and Render tests...\n")
os.chdir("C:\\Users\\Batarda\\Desktop\\Python-Screwery\\TerminalGraphicsModule")
world = {}
world = World.loadModel("Model.txt", world)
World.printWorld(world)
input("Cleared?\n")
os.system("cls")
input("Starting Raytrace tests...\n")
clippingplane = []
clippingplane = Render.createClippingplane(float(input("Width of clipping plane?\n")),screen,float(input("Clipping plane distance?\n")))
print("clippingplane =", clippingplane)
input("Cleared?\n")
os.system("cls")
projection = {}
projection = Render.createProjection(world,clippingplane)
World.printWorld(projection)
input("Cleared?\n")
projectedtoscreen = Render.ProjectiontoScreen(projection,screen,clippingplane)