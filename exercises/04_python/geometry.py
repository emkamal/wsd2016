import math

class Point:
	x = y = distanceFrom = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def distance_from(self, otherPoint):
		deltaX = self.x - otherPoint.x
		deltaY = self.y - otherPoint.y
		return math.sqrt(deltaX*deltaX + deltaY*deltaY)
		
class Circle:
	
	radius = 0
	
	def __init__(self, center, radius):
		self.center = centerPoint
		self.radius = radius
		
	def is_inside(self, otherPoint):
		d = self.center.distance_from(otherPoint);
		
		if d <= self.radius:
			return True
		else:
			return False