import os

def createClippingplane(width,screen,distance):
	##FINDING ASPECT RATIO OF SCREEN
	aspectratio = len(screen)/len(screen[0])
	##3-VALUE ARRAY REPRESENTING X WIDTH, Y HEIGHT, and Z DISTANCE!
	clippingplane = [width,width*aspectratio,distance]
	#print(clippingplane)
	return clippingplane

def projectVertex(vertex, clippingplane):
	unitvector = [0]*3
	projectedvertex = [0]*3
	for i in range(len(vertex)):
		unitvector[i] = vertex[i]/(((vertex[0]**2)+(vertex[1]**2)+(vertex[2]**2))**0.5)
	if unitvector[2] != 0:
		t = clippingplane[2]/unitvector[2]
		for i in range(len(vertex)):
			projectedvertex[i] = unitvector[i]*t
	else:
		projectedvertex = [-100,-100,"ERROR"]
	return projectedvertex
	
##WHEN ONE CHOOSES THE VERTICES TO RENDER, REMEMBER THAT THE RETURN VALUE IS --NOT-- IN ORDER. USE createProjection AFTER THIS!
##Also worth noting that, at the moment, optimization methods are very rudimentary - all that is being done is excluding those behind the clippingplane.
##Feels bad.
def chooseVertices(world, clippingplane):
	worldkeys = []
	worldkeys = list(world.keys())
	for i in range(len(worldkeys)):
		if world[worldkeys[i]][2] < clippingplane[2]:
			del world[worldkeys[i]]
	return world
	
##createProjection is recommended because it does not require one to specify the keys within the world dictionary!
def createProjection(world, clippingplane):
	projection = {}
	for key in world:
		projection[key] = projectVertex(world[key], clippingplane)
	return projection
	
def ProjectiontoScreen(projection, screen, clippingplane):
	"""
	Projection to Screen works by first eliminating all the vertices which lie outside of the clipping plane
	"""
	
	
	return screen
	
##DEBUG ZONE
"""
input("ENTERING DEBUG\n")
screen = [[0]*5,[0]*5,[0]*5]
clippingplane = createClippingplane(float(input("Clipping Plane Width? (height calculated automatically)\n")),screen,float(input("Clipping Plane Distance?\n")))
projectedvertex = projectVertex([float(input("x?")),float(input("y?")),float(input("z?"))],clippingplane)
print(projectedvertex)
input("DONE")
"""