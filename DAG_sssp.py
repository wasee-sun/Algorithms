from Topological_sort import Topsort
import random
#* Directed Acylic Graph
        
    
def sssp(graph):
    tps = Topsort(graph, True)
    top_arr = tps.top_sort()
    short_path_dict = {}
    for ele in top_arr:
        short_path_dict[ele] = 0
    for ele in top_arr:
        short_path_dict = _sssp(ele, short_path_dict, graph)
        
    return short_path_dict
        
def _sssp(ele, spd, graph):
    ele_arr = graph[ele]
    for node, edge in ele_arr:
        if ((spd[node] == 0) or (spd[node] > spd[ele] + edge)):
            spd[node] = spd[ele] + edge
    
    return spd
    
def lssp(graph):
    tps = Topsort(graph, True)
    top_arr = tps.top_sort()
    short_path_dict = {}
    for ele in top_arr:
        short_path_dict[ele] = 0
    for ele in top_arr:
        short_path_dict = _lssp(ele, short_path_dict, graph)
    for ele in top_arr:
        short_path_dict[ele] *= -1
        
    return short_path_dict

def _lssp(ele, spd, graph):
    ele_arr = graph[ele]
    for node, edge in ele_arr:
        edge *= -1
        if ((spd[node] == 0) or (spd[node] > spd[ele] + edge)):
            spd[node] = spd[ele] + edge
    
    return spd

if __name__ == '__main__':
    graph = {
        "A" : [("B", 3), ("C", 6)],
        "B" : [("E", 11), ("D", 4), ("C", 4)],
        "C" : [("D", 8), ("G", 11)],
        "D" : [("E", -4), ("F", 5), ("G", 2)],
        "E" : [("H", 9)],
        "F" : [("H", 1)],
        "G" : [("H", 2)],
        "H" : [],
    }
    
    print(sssp(graph))
    print(lssp(graph))