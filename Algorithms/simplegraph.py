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
        while not queue.empty():
            curr = queue.get()
            if curr not in visited:
                print curr
                visited.append(curr)
            	for adj in self.nodes[curr]:
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
                        return True, visited
                    else:
                        queue.put(adj)
        return False

    def topo_sort(self, node, solution):
        for dep in self.nodes[node]:
            self.topo_sort(dep, solution)
        if node not in solution:
            solution.append(node)
        return solution

    def topological_sort(self, node):
        return self.topo_sort(node, [])

if __name__ == "__main__":

    graph = {'A': ['B', 'C', 'D'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['E'],
             'E': ['K', 'I', 'J'],
             'K': [],
             'I': ['J'],
             'J': []}

    g = Graph()
    g.load_graph(graph)

    g.breadthfs('A')
    print ""
    g.breadthfs('A')
    print g.are_connected('A', 'F')

    print g.topological_sort('A')
