class Node():
	def __init__(self, value, adjacents):
		self.value     = value
		self.adjacents = adjacents
		self.visited   = False

class Edge():
	def __init__(self, nodeA, nodeB, weight):