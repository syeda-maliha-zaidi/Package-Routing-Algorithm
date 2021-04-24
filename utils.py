from graph import Vertex, Graph
from sys import maxsize 
from itertools import permutations

# Creates a graph of the addresses and their weights being the distance between them
# Time complexity is O(N^2)
def create_address_graph(address_data, distance_data):

    graph_verticies = [Vertex(address) for address in address_data]

    g = Graph()

    for graph_vertex in graph_verticies:
        g.addVertex(graph_vertex)

    # Time complexity is O(N^2)
    for idx, distance_row in enumerate(distance_data):
        for i in range(0, len( distance_row )):
            if distance_row[i] == '':
                break

            g.addUndirectedEdge( graph_verticies[idx], graph_verticies[i], float(distance_row[i] ) )

    return g


# Helper function to convert minutes into a string of readable time in the form (HH:MM)
# Complexity is O(1)
def minutes_to_time(mins):
    time = "{:02d}:{:02d}".format(int(mins / 60), mins % 60)
    return time