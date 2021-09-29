# Implement a graph using Node class and adjacency list
from collections import OrderedDict


class Node:

    def __init__(self, key):

        self.key = key
        self.connections = OrderedDict()

    def __str__(self):
        return str(self.key)

    def add_neighbor(self, nbr, weight=0):

        self.connections[nbr] = weight

    def get_connections(self):

        return self.connections.keys()

    def get_id(self):

        return self.key

    def get_weight(self, nbr):

        return self.connections[nbr]


class Graph:

    def __init__(self):

        self.vertices = {}
        self.numVerts = 0

    def add_vert(self, key):

        self.numVerts += 1
        newVertex = Node(key)
        self.vertices[key] = newVertex
        return newVertex

    def get_vert(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def add_edge(self, start, end, weight):

        if start not in self.vertices:
            new = self.add_vert(start)
        if end not in self.vertices:
            new = self.add_vert(end)

        self.vertices[start].add_neighbor(self.vertices[end], weight)

    def get_vertices(self):

        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, item):

        return item in self.vertices


graph = Graph()

for i in range(6):
    graph.add_vert(i)

graph.add_edge(0, 2, 5)
graph.add_edge(2, 3, 4)
graph.add_edge(1, 3, 6)
graph.add_edge(1, 6, 9)

for edge in graph.vertices[1].get_connections():
    print(graph.vertices[1].get_weight(edge))
