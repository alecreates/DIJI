import sys
import math


INF = math.inf

class Vertex:
    def __init__(self, n):
        self.name = n
        #stores the names of the vertex's neighbor vertices
        self.neighbors = []

#don't forget to credit the creator of this code
class Graph:
    #initialize new instance of a Graph with empty set of vertices
    
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False
        
    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            self.vertices[u].neighbors.append(v)
            self.vertices[v].neighbors.append(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end = '')
            print(' ')

    def get_weight(self, u, v):
        if u in self.vertices and v in self.vertices:
            return self.edges[self.edge_indices[u]][self.edge_indices[v]]

    def get_neighbors(self, u):
        return self.vertices[u].neighbors

        
    #Returns shortest path to each vertex from the specified source using Dijkstra's algorithm.
    def shortest_path(self, source):
        unvisited_nodes = list(self.vertices)
        shortest_path = {}
        #previous_nodes = {}
        max_value= sys.maxsize
        for i in unvisited_nodes:
            shortest_path[i] = max_value
        shortest_path[source] = 0
        while unvisited_nodes:
            current_min_node = None
            #finds current vertex with the smallest value
            for i in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = i
                elif shortest_path[i] < shortest_path[current_min_node]:
                    current_min_node = i
            neighbors = self.get_neighbors(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.get_weight(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    #previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return shortest_path
   

   