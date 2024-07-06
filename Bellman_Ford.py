# from Data_structure.Stack_Queue_Deque import Queue
from Data_structure.priority_queue_graph import Priority_Queue
import numpy as np


def bellman_ford(graph, st_idx):
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    dist_arr = [np.inf for i in range(len(graph))]
    dist_arr[graph[st_idx][1]] = 0
    Q = Priority_Queue()
    for i in range(len(graph)):
        Q.enqueue((st_idx, 0))
        visited = [False for i in range(len(graph))]
        if i == len(graph) - 1:
            dist_arr = _bellman_ford(graph, dist_arr, Q, visited, True)
        else:
            dist_arr = _bellman_ford(graph, dist_arr, Q, visited)
    
    return dist_arr
    
def _bellman_ford(graph, dist_arr, Q, visited, ng_cycle = False):
    while not Q.is_empty():
        node = Q.dequeue()
        if visited[graph[node[0]][1]] == True:
            continue
        visited[graph[node[0]][1]] = True
        for edge in graph[node[0]][0]:
            if ((dist_arr[graph[edge[0]][1]] == np.inf) or 
                (dist_arr[graph[edge[0]][1]] > dist_arr[graph[node[0]][1]] + edge[1])):
                if ng_cycle:
                    dist_arr[graph[edge[0]][1]] = - np.inf
                else:
                    dist_arr[graph[edge[0]][1]] = dist_arr[graph[node[0]][1]] + edge[1]
                                    
            Q.enqueue(edge)
            
    return dist_arr



if __name__ == '__main__':
    graph = {
        0 : [(1, 5)],
        1 : [(2, 20), (5, 30), (6, 60)],
        2 : [(3, 10), (4, 75)],
        3 : [(2, -15)],
        4 : [(9, 100)],
        5 : [(6, 5), (4, 25), (8, 50)],
        6 : [(7, -50)],
        7 : [(8, -10)],
        8 : [],
        9 : []
    }
    
    print(bellman_ford(graph, 0))
    