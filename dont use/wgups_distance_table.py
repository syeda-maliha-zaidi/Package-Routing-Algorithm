from graph import Vertex, Graph, HashGraph
import csv

def load_distance_graph():
    g = Graph()
    hg = None

    with open('distances.csv', newline='') as csvfile:
        distances_list = list(csv.reader(csvfile, delimiter=','))

        graph_verticies = [Vertex(distance_row[0]) for distance_row in distances_list]

        hg = HashGraph(len(graph_verticies))

        for graph_vertex in graph_verticies:
            g.add_vertex(graph_vertex)
            hg.add_vertex(graph_vertex)

        for idx, distance_row in enumerate(distances_list):
            for i in range(1, len( distance_row )):
                if distance_row[i] == '0.0':
                    continue

                g.add_undirected_edge( graph_verticies[idx], graph_verticies[i-1], distance_row[i] )
                hg.add_undirected_edge( graph_verticies[idx], graph_verticies[i-1], distance_row[i] )

    return g, hg