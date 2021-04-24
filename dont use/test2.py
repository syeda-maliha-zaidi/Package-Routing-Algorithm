# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
from itertools import permutations
V = 13
 
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
 
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
         
    return min_path 
 
 
# Driver Code 
if __name__ == "__main__": 
 
    # matrix representation of graph 
    graph= [[ 0, 10, 15, 20, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 10, 0, 35, 25, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 15, 35, 0, 30, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 20, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 23, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 2, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 42, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 70, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90], 
            [ 50, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ],
            [ 50, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 50, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 50, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 50, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ], 
            [ 50, 25, 30, 0, 50, 90, 42, 25, 30, 0, 50, 90, 30, 0, 50, 90 ]] 
    s = 0
    print(travellingSalesmanProblem(graph, s))