from view.view_const import *
from model.sample_mazes import *

class BlockState:
	
	def __init__(self, x, y, x2, y2, maze):
		self.x = x
		self.y = y
		self.x2 = x2
		self.y2 = y2
		self.maze = maze
		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __ne__(self, other):
		return not self.__eq__(other)
		
	def __hash__(self):
		return hash((x,y,x2,y2))
		
	def __str__(self):
		return f"{self.x} , {self.y} : {self.x2} , {self.y2}"
	

	def isStanding(self):
		return self.x == self.x2 and self.y == self.y2
	
	def isYtopX(self):  # Y is on top of X
		return self.x == self.x2 and self.y2 < self.y
	
	def isXtopY(self):  # X is on top of Y
		return self.x == self.x2 and self.y2 > self.y
	
	def isYrightX(self):  # Y is on right of X
		return self.y == self.y2 and self.x2 > self.x
	
	def isXrightY(self):  # X is on right of Y
		return self.y == self.y2 and self.x2 < self.x
	
	def checkIfCanMove(self):
		if self.x > MATRIX_ROW-1 or self.x < 0 or self.y > MATRIX_COL-1 or self.y < 0:
			return False  # out of bounds
		if self.x2 > MATRIX_ROW-1 or self.x2 < 0 or self.y2 > MATRIX_COL-1 or self.y2 < 0:
			return False  # out of bounds
		a = self.maze[self.x + self.y * MATRIX_COL] not in INVALID_NODES
		b = self.maze[self.x2 + self.y2 * MATRIX_COL] not in INVALID_NODES
		return a and b
	
		
