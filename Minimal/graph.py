#!/usr/bin/python
import Queue

class Node():

    def __init__(self, value, adjacents):
        self.value = value
        self.adjacents = adjacents
        self.visited = False


class Edge():

    def __init__(self, nodeB, weight=0):
        self.to = nodeB
        self.weight = weight


class Graph():
	def __init__(self):
		self.nodes = []


	def insert(self, node):
		self.nodes.append(node)
