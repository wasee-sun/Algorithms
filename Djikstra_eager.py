from Data_structure.idx_pq import Idx_Priority_Queue
import numpy as np


def dijkstra(graph, start):
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    dist_arr = [np.inf for i in range(len(graph))]
    prev = [None for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    dist_arr[graph[start][1]] = 0
    IPQ = Idx_Priority_Queue(graph)
    IPQ.enqueue((start, 0))
    return _dijkstra(graph, dist_arr, prev, visited, IPQ)
    
def _dijkstra(graph, dist_arr, prev, visited, IPQ):
    while not IPQ.is_empty():
        node = IPQ.dequeue()
        if visited[graph[node[0]][1]] == True:
            continue
        visited[graph[node[0]][1]] = True
        if dist_arr[graph[node[0]][1]] >= node[1]:
            for edge in graph[node[0]][0]:
                if ((dist_arr[graph[edge[0]][1]] == np.inf) or 
                    (dist_arr[graph[edge[0]][1]] > dist_arr[graph[node[0]][1]] + edge[1])):
                    dist_arr[graph[edge[0]][1]] = dist_arr[graph[node[0]][1]] + edge[1]
                    prev[graph[edge[0]][1]] = node[0]
                                        
                IPQ.enqueue(edge)
                
    return dist_arr, prev

def shortest_path(graph, start, end):
    dist_arr, prev = dijkstra(graph, start)
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
        "A" : [("B", 5), ("C", 1)],
        "B" : [("C", 2), ("D", 3), ("E", 20)],
        "C" : [("B", 3), ("E", 12)],
        "D" : [("C", 3), ("E", 2), ("F", 6)],
        "E" : [("F", 1)],
        "F" : []
    }
    
    # Test code for IDX priority Queue
    # IPQ = Idx_Priority_Queue(graph)
    # IPQ.enqueue(("B", 5))
    # IPQ.enqueue(("C", 1))
    # IPQ.enqueue(("A", 0))
    # IPQ.enqueue(("D", 3))
    # IPQ.enqueue(("E", 7))
    # IPQ.enqueue(("F", 2))
    # print(IPQ.queue.heap, IPQ.queue.ps)
    # IPQ.dequeue()
    # print(IPQ.queue.heap, IPQ.queue.ps)
    # IPQ.enqueue(("A", 1))
    # print(IPQ.queue.heap, IPQ.queue.ps)
    
    print(dijkstra(graph, "A"))
    print(shortest_path(graph, "A", "F"))