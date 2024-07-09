from Topological_sort import Topsort


def kosaraju(graph):
    tps = Topsort(graph)
    tps_arr = tps.top_sort()
    graph = transpose_graph(graph)
    visited = [-1 for i in range(len(graph))]
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    scc_eles = []
    scc = 0
    while len(sum(scc_eles, [])) != len(graph):
        start = [item for item in tps_arr if item not in sum(scc_eles, [])]
        new_completed, visited = _kosaraju(graph, start[0], visited)
        scc_eles.append(new_completed)
        scc += 1
        
    return scc, scc_eles
    
def _kosaraju(graph, node, visited):
    visited[graph[node][1]] = 0
    scc_eles = []
    for nxt_node in graph[node][0]:
        if visited[graph[nxt_node][1]] == -1:
            scc_eles, visited = _kosaraju(graph, nxt_node, visited)
        if visited[graph[nxt_node][1]] == 0:
            scc_eles.append(nxt_node)
            visited[graph[nxt_node][1]] = 1
            return scc_eles, visited
        
    scc_eles.append(node)
    visited[graph[node][1]] = 1
    return scc_eles, visited
            
def transpose_graph(graph):
    n_graph = {key : [] for key in graph.keys()}
    for key, vals in graph.items():
        for val in vals:
            n_graph[val].append(key)
    return n_graph


if __name__ == '__main__':
    graph = {
        "A" : ["B"],
        "B" : ["D"],
        "C" : ["A", "D"],
        "D" : ["E", "F"],
        "E" : ["B", "F", "G"],
        "F" : ["H"],
        "G" : ["F"],
        "H" : ["G"],
    }
    print(kosaraju(graph))