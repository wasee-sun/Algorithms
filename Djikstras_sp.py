from Data_structure.priority_queue_graph import Priority_Queue
import numpy as np


def dijkstra(graph, st_idx):
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    dist_arr = [np.inf for i in range(len(graph))]
    prev = [None for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    dist_arr[graph[st_idx][1]] = 0
    PQ = Priority_Queue()
    PQ.enqueue((st_idx, 0))
    return _dijkstra(graph, dist_arr, prev, visited, PQ)
    
def _dijkstra(graph, dist_arr, prev, visited, PQ):
    while not PQ.is_empty():
        node = PQ.dequeue()
        if visited[graph[node[0]][1]] == True:
            continue
        visited[graph[node[0]][1]] = True
        if dist_arr[graph[node[0]][1]] >= node[1]:
            for edge in graph[node[0]][0]:
                if ((dist_arr[graph[edge[0]][1]] == np.inf) or 
                    (dist_arr[graph[edge[0]][1]] > dist_arr[graph[node[0]][1]] + edge[1])):
                    dist_arr[graph[edge[0]][1]] = dist_arr[graph[node[0]][1]] + edge[1]
                    prev[graph[edge[0]][1]] = node[0]
                                        
                    PQ.enqueue(edge)
                
    return dist_arr, prev

def shortest_path(graph, st_idx, end):
    dist_arr, prev = dijkstra(graph, st_idx)
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    if dist_arr[graph[end][1]] == np.inf:
        return None
    else:
        cur_node = end
        path = [end]
        while prev[graph[cur_node][1]] != None:
            cur_node = prev[graph[path[0]][1]]  
            path = [cur_node] + path
        return path


if __name__ == '__main__':
    graph = {
        0 : [(1, 4), (2, 1)],
        1 : [(3, 1)],
        2 : [(1, 2), (3, 5)],
        3 : [(4, 3)],
        4 : []
    }

    print(dijkstra(graph, 0))
    print(shortest_path(graph, 0, 4))
    