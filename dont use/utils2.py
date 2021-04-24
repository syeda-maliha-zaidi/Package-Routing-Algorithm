from graph import Vertex, Graph
from sys import maxsize 
from itertools import permutations

class HashGraph:
    def __init__(self, size):
        self.adjacency_list = ChainingHashTable(size)
        self.edge_weights = ChainingHashTable(size)
        
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def get_vertex(self, vertex_lbl):
        for vert in self.adjacency_list:
            if vert.label == vertex_lbl:
                return vert
        return None
        
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def __str__(self):
        adjacency_list_str = adjacency_list.join()
        return "Adjacency List: {0}\n\nEdge Weights: {1}\n\n".format( str(self.adjacency_list), str(self.edge_weights) )

def create_address_graph(address_data, distance_data):

    graph_verticies = [Vertex(address) for address in address_data]

    g = Graph()

    for graph_vertex in graph_verticies:
        g.add_vertex(graph_vertex)

    for idx, distance_row in enumerate(distance_data):
        for i in range(0, len( distance_row )):
            if distance_row[i] == '':
                break

            g.add_undirected_edge( graph_verticies[idx], graph_verticies[i], float(distance_row[i] ) )

    return g

def travellingSalesmanProblem(graph, addresses_list, start_address): 
 
    # store all vertex apart from source vertex 
    vertex = [] 
    min_visited = []
    visited = []


    s = graph.get_vertex(start_address)

    for v in graph.get_vertex_list(): 
        if v != s and v.label in addresses_list: 
            vertex.append(v) 
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
        visited = []
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            visited.append(j)
            current_pathweight += graph.get_edge(k, j)
            k = j 
        current_pathweight += graph.get_edge(k,s) 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
        if min_path == current_pathweight:
            min_visited = visited

    print(min_path)
    print(min_visited)

    min_visited.insert(0,s)
    min_visited.append(s)
         
    return min_visited, min_path 

def shortest_path(graph, addresses_list, start_address):
    neighbor = 0
    unvisited = []
    visited = []
    total_weight = 0

    start_node = graph.get_vertex(start_address)
    current_node = start_node

    vertex_list = graph.get_vertex_list()

    for vertex in vertex_list:
        if vertex == start_node:
            visited.append(start_node)
        elif vertex.label in addresses_list:
            unvisited.append(vertex)

    next_permutation=permutations(unvisited)

    #for permuatation in next_permutation:
    while unvisited:
        for index, neighbor in enumerate(unvisited):
            if index == 0:
                current_weight = graph.get_edge(start_node, neighbor)
                current_node = neighbor
            elif graph.get_edge(current_node, neighbor) < current_weight:
                current_weight = graph.get_edge(current_node, neighbor)
                current_node = neighbor
        total_weight += current_weight
        unvisited.remove(current_node)
        visited.append(current_node)

    return visited, total_weight

def compute_truck_route(graph, package_list):    
    
    def get_next_location(graph, current_address, package_list):
        min_distance = maxsize
        next_package_to_deliver = None
        next_address = None

        current_location_vertex = graph.get_vertex( current_address )

        for package in package_list:
            package_vertex = graph.get_vertex( package.getAddress() )
            edge_weight = graph.get_edge(current_location_vertex, package_vertex)

            if edge_weight < min_distance:
                min_distance = edge_weight
                next_package_to_deliver = package
                next_address = package.getAddress()
                
        return next_package_to_deliver, next_address, min_distance

    address_to_visit = "4001 South 700 East"
    hub_vertex = graph.get_vertex(address_to_visit)
    total_route_dist = 0

    temp_list = list( package_list )

    for i in range( len(package_list) ):
        next_package, address_to_visit, dist_to_travel = get_next_location(graph, address_to_visit, temp_list)

        temp_list.remove( next_package )

        total_route_dist += dist_to_travel

    total_route_dist += graph.get_edge(hub_vertex, graph.get_vertex(address_to_visit))

    print( total_route_dist)



# def get_next_location(graph, current_address, package_list):
#     min_distance = maxsize
#     next_package_to_deliver = None
#     next_address = None

#     current_location_vertex = graph.get_vertex( current_address )

#     for package in package_list:
#         package_vertex = graph.get_vertex( package.getAddress() )
#         edge_weight = graph.get_edge(current_location_vertex, package_vertex)

#         if edge_weight < min_distance:
#             min_distance = edge_weight
#             next_package_to_deliver = package
#             next_address = package.getAddress()

#     return next_package_to_deliver, next_address, min_distance

# def shortest_path(node_list, edges, start):
#     neighbor = 0
#     unvisited = []
#     visited = []
#     total_weight = 0
#     current_node = start
#     for node in node_list:
#         if node[2] == start:
#             visited.append(start)
#         else:
#             unvisited.append(node[2])
#     while unvisited:
#         for index, neighbor in enumerate(unvisited):
#             if index == 0:
#                 current_weight = edges[start, neighbor]
#                 current_node = neighbor
#             elif edges[start, neighbor] < current_weight:
#                 current_weight = edges[start, neighbor]
#                 current_node = neighbor
#         total_weight += current_weight
#         unvisited.remove(current_node)
#         visited.append(current_node)
#     return visited, total_weight


# def create_sub_graph_with_packages(address_data, distance_data, package_list):
#     graph_verticies = []
#     g = Graph()

#     # Always add the hub as the start
#     graph_verticies.append( Vertex("4001 South 700 East") )

#     for address in address_data:
#         for package in package_list:
#             if package.getAddress() == address:
#                 graph_verticies.append( Vertex(address ) )

#     for graph_vertex in graph_verticies:
#         g.add_vertex(graph_vertex)

#     for idx, distance_row in enumerate(distance_data):
#         for i in range(0, len( distance_row )):
#             if distance_row[i] == '0.0':
#                 break

#             g.add_undirected_edge( graph_verticies[idx], graph_verticies[i], distance_row[i] )

#     return g

# V = 4
 
# # implementation of traveling Salesman Problem 
# def travellingSalesmanProblem(graph, start_vertex): 
 
#     # store all vertex apart from source vertex 
#     vertex = [] 
#     for i in range(graph.get_vertex_count()): 
#         if i != s: 
#             vertex.append(i) 
 
#     # store minimum weight Hamiltonian Cycle 
#     min_path = maxsize 
#     next_permutation=permutations(vertex)
#     for i in next_permutation:
 
#         # store current Path weight(cost) 
#         current_pathweight = 0
 
#         # compute current path weight 
#         k = s 
#         for j in i: 
#             current_pathweight += graph[k][j] 
#             k = j 
#         current_pathweight += graph[k][s] 
 
#         # update minimum 
#         min_path = min(min_path, current_pathweight) 
         
#     return min_path 
 
 
# # Driver Code 
# if __name__ == "__main__": 
 
#     # matrix representation of graph 
#     graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
#             [15, 35, 0, 30], [20, 25, 30, 0]] 
#     s = 0
#     print(travellingSalesmanProblem(graph, s))