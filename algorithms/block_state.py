
class BlockState:
	
	def __init__(self, x, y, x2, y2):
		self.x = x
		self.y = y
		self.x2 = x2
		self.y2 = y2
		
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
		
