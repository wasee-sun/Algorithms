# Algorithms
from Data_structure.Stack_Queue_Deque import Stack, Queue


#Creating Adjacency Matrix from Input file
def adj_matrix():
    with open(f"input.txt", "r") as f1:
        vertices, edges = f1.readline().strip().split()
        matrix = [[0 for i in range(int(vertices) + 1)] for i in range(int(vertices) + 1)]
        for i in range(int(edges)):
            u, v, w = f1.readline().strip().split()
            matrix[int(u)][int(v)] = int(w)
        print(matrix)
        with open(f"output.txt", "w") as f2:
            for i in range(int(vertices) + 1):
                for j in range(int(vertices) + 1):
                    f2.write(f"{matrix[i][j]} ")
                f2.write("\n")
                
                
#Creating Adjacency List from Input file
def adj_list():
    with open(f"input.txt", "r") as f1:
        vertices, edges = f1.readline().strip().split()
        diction = {i:[] for i in range(int(vertices) + 1)}
        for i in range(int(edges)):
            u, v, w = f1.readline().strip().split()
            diction[int(u)].append((int(v), int(w)))
        print(diction)
        with open(f"output1.txt", "w") as f2:
            for key, val in diction.items():
                f2.write(f"{key} : ")
                for value in val:
                    f2.write(f"{value} ")
                f2.write(f"\n")
                    

#! Graph algorithms
#Used on both unweighted and weighted graphs
def dfs(graph, start):
    visited = [False for i in range(len(graph))] 
    return _dfs(graph, start, visited, [])
    
def _dfs(graph, node, visited, path):
    visited[node] = True
    path.append(node)
    
    for val in graph[node]:
        if visited[val] == False:
            path = _dfs(graph, val, visited, path)
        
    return path
        
        
# Used mainly on unweighted graphs
def bfs(graph, start):
    visited = [False for i in range(len(graph))] 
    Q = Queue()
    visited[start] = True
    Q.enqueue(start)
    bfs_arr = []
    
    while not Q.is_empty():
        node = Q.dequeue()
        bfs_arr.append(node)
        for val in graph[node]:
            if visited[val] == False:
                visited[val] = True
                Q.enqueue(val)
                
    return bfs_arr

    
if __name__ == '__main__':
    graph = {
        0: [1], 
        1: [9, 5], 
        2: [], 
        3: [9, 8, 7], 
        4: [], 
        5: [4, 3, 6], 
        6: [], 
        7: [4], 
        8: [2, 6], 
        9: [4, 8, 9]
    }
    
    print(dfs(graph, 0))
    print(bfs(graph, 0))
    
    
    