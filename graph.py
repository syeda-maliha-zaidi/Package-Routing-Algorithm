
# Stores a vertex location as a label
class Vertex:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return "(Vertex) {0}".format( self.label )

    def __str__(self):
        return "{0}".format( self.label )
        
# Graph with verticies
# Used to store the addresses and their connections
class Graph:
    def __init__(self):
        self.verticies = {}
        self.edges = {}
       
    # Adds vertex to list
    # Complexity is O(1)
    def addVertex(self, new_vertex):
        self.verticies[new_vertex] = []

    # Returns the vertex with the specific label
    # Complexity is O(n)
    def getVertex(self, vertex_lbl):
        for vert in self.verticies:
            if vert.label == vertex_lbl:
                return vert
        return None

    # Returns the edge for the specific tuple of vertex objects
    # Complexity is O(1)
    def getEdge(self, from_vertex, to_vertex):
        return self.edges[(from_vertex, to_vertex)]
        
    # Adds directed edge to list
    # Complexity is O(1)
    def addDirectedEdge(self, from_vertex, to_vertex, weight = 1.0):
        self.edges[(from_vertex, to_vertex)] = weight
        self.verticies[from_vertex].append(to_vertex)
    
    # Adds undirected edge to list
    # Complexity is O(1)
    def addUndirectedEdge(self, vertex_a, vertex_b, weight = 1.0):
        self.addDirectedEdge(vertex_a, vertex_b, weight)
        self.addDirectedEdge(vertex_b, vertex_a, weight)

    def __str__(self):
        return "Adjacency List: {0}\n\nEdge Weights: {1}\n\n".format( str(self.verticies), str(self.edges) )