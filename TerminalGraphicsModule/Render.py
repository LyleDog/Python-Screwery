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
	
def chooseVertices(world, clippingplane):
	
	return world
	
def createProjection(world, clippingplane):
	projection = {}
	for i in range(1,len(world)):
		projection["vert{}".format(i)] = projectVertex(world["vert{}".format(i)], clippingplane)
	return projection
	
def ProjectiontoScreen(projection, screen, clippingplane):
	"""
	Projection to Screen works by first eliminating all the vertices which lie outside of the clipping plane
	"""
	
	
	return screen
	
##DEBUG ZONE

input("ENTERING DEBUG\n")
screen = [[0]*5,[0]*5,[0]*5]
clippingplane = createClippingplane(float(input("Clipping Plane Width? (height calculated automatically)\n")),screen,float(input("Clipping Plane Distance?\n")))
projectedvertex = projectVertex([float(input("x?")),float(input("y?")),float(input("z?"))],clippingplane)
print(projectedvertex)
input("DONE")
