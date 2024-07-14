from Data_structure.priority_queue_graph import Priority_Queue
import numpy as np


def prim_mst(graph, start):
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    visited = [False for i in range(len(graph))]
    mst_path = [np.inf for i in range(len(graph))]
    PQ = Priority_Queue()
    for edge, weight in graph[start][0]:
        PQ.enqueue(((start, edge), weight))
    
    visited[graph[start][1]] = True
    mst_path[graph[start][1]] = 0
    
    while not PQ.is_empty():
        nodes, node_weight = PQ.dequeue()
        if visited[graph[nodes[1]][1]] == False: # nodes[1] is the destination node
            mst_path[graph[nodes[1]][1]] = node_weight
            for edge, weight in graph[nodes[1]][0]:
                PQ.enqueue(((nodes[1], edge), weight))
            
            visited[graph[nodes[1]][1]] = True
        
    return sum(mst_path)


if __name__ == '__main__':
    graph = {
        "A" : [("B", 10), ("C", 1), ("D", 4)],
        "B" : [("A", 10), ("C", 3), ("E", 0)],
        "C" : [("A", 1), ("B", 3), ("D", 2), ("F", 8)],
        "D" : [("A", 4), ("B", 2), ("F", 2), ("G", 7)],
        "E" : [("B", 0), ("F", 1), ("H", 8)],
        "F" : [("B", 8), ("C", 2), ("E", 1), ("G", 6), ("H", 9)],
        "G" : [("C", 7), ("F", 6), ("H", 12)],
        "H" : [("E", 8), ("F", 9), ("G", 12)]
    }
    
    print(prim_mst(graph, "A"))