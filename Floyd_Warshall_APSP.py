import numpy as np

#only shortest distance
def floyd_warshall(graph):
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    dist = [[np.inf for j in range(len(graph))] for i in range(len(graph))]
    
    for i in range(len(graph)):
        dist[i][i] = 0
        
    for key, vals in graph.items():
        for val in vals[0]:
            dist[graph[key][1]][graph[val[0]][1]] = val[1]
            
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

# Determine negative cycles
def negative_cycle(dist, length):
    flag = False
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = - np.inf
                    flag = True
                    
    return dist, flag
    

# shortest distance with path
# Not usable if there are negative cycles
def floyd_warshall_sp(graph):
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    dist = [[[np.inf, []] for j in range(len(graph))] for i in range(len(graph))]
    
    for i in range(len(graph)):
        dist[i][i][0] = 0
        dist[i][i][1] = []
        
    for key, vals in graph.items():
        for val in vals[0]:
            dist[graph[key][1]][graph[val[0]][1]][0] = val[1]
            dist[graph[key][1]][graph[val[0]][1]][1] = [key, val[0]]
            
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][j][0] > dist[i][k][0] + dist[k][j][0]:
                    dist[i][j][0] = dist[i][k][0] + dist[k][j][0]
                    dist[i][j][1] = dist[i][k][1] + dist[k][j][1][1:]
                    
    return dist




if __name__ == '__main__':
    graph = {
        "A" : [("C", -2)],
        "B" : [("A", 4), ("C", 3)],
        "C" : [("D", 2)],
        "D" : [("B", -1)]
    }
    
    # answer of the above graph
    # ans = [
    #     [[0, []], [-1, ['A', 'C', 'D', 'B']], [-2, ['A', 'C']], [0, ['A', 'C', 'D']]], 
    #     [[4, ['B', 'A']], [0, []], [2, ['B', 'A', 'C']], [4, ['B', 'A', 'C', 'D']]], 
    #     [[5, ['C', 'D', 'B', 'A']], [1, ['C', 'D', 'B']], [0, []], [2, ['C', 'D']]], 
    #     [[3, ['D', 'B', 'A']], [-1, ['D', 'B']], [1, ['D', 'B', 'A', 'C']], [0, []]]
    #     ]
    
    matrix = floyd_warshall(graph)
    print(matrix)
    print(negative_cycle(matrix, len(graph)))
    print(floyd_warshall_sp(graph))