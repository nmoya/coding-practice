#!/usr/bin/python
import Queue

class Graph():

    def __init__(self):
        self.nodes = {}

    def load_graph(self, graph):
    	''' A python dictionary. Each key is a node with a list of edges '''
        self.nodes = graph

    def breadthfs(self, start):
    	''' Breadth First Search in the graph '''
        queue = Queue.Queue()
        visited = []
        queue.put(start)
        visited.append(start)
        print start

        while not queue.empty():
        	curr = queue.get()
        	for adj in self.nodes[curr]:
        		if adj not in visited:
        			print adj
        			visited.append(adj)
        			queue.put(adj)

    def _depthfs(self, node, visited):
    	''' Depth First Search in the graph '''
    	if node in visited:
    		return
    	else:
    		print node
    		visited.append(node)
    		for adj in self.nodes[node]:
    			if adj not in visited:
    				self._depthfs(adj, visited)

    def depthfs(self, start):
    	self._depthfs(start, [])

    def are_connected(self, nodeA, nodeB):
        visited = []
        queue = Queue.Queue()
        queue.put(nodeA)
        visited.append(nodeA)

        while not queue.empty():
            curr = queue.get()
            for adj in self.nodes[curr]:
                if adj not in visited:
                    visited.append(adj)
                    if adj == nodeB:
                        return True
                    else:
                        queue.put(adj)
        return False


if __name__ == "__main__":

    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['E'],
             'E': ['C'],
             'F': ['C']}

    g = Graph()
    g.load_graph(graph)

    g.breadthfs('A')
    print ""
    g.breadthfs('A')
    print g.are_connected('A', 'F')
