import random

#! Topsort using adjacency list
#! Can only be used in a DAG (Directed Acyclic Graph)
class Topsort:
    def __init__(self, graph, weighted = False):
        if weighted:
            self.graph = {key : [] for key in graph.keys()}
            for key, vals in graph.items():
                for val in vals:
                    self.graph[key].append(val[0])
        else:
            self.graph = graph
        self.graph_id = {key : j for key, j in zip(graph.keys(), range(len(graph)))}
        self.top_arr = [0] * len(self.graph)
        self.idx = len(self.graph) - 1
        
    def top_sort(self):
        visited_lst = [False for i in range(len(self.graph))]
        explored_lst = [False for i in range(len(self.graph))]
            
        while True:
            val = list(self.graph.keys() - self.top_arr)
            if len(val) == 0:
                break
            r_key = random.choice(val) # depending on random choice
            explored_lst, visited_lst = self._top_sort(r_key, explored_lst, visited_lst)
            
        return self.top_arr
            
    def _top_sort(self, cur_key, explored_lst, visited_lst): #* dfs
        visited_lst[self.graph_id[cur_key]] = True
        for val in self.graph[cur_key]:
            if ((explored_lst[self.graph_id[val]] is False) and 
            (visited_lst[self.graph_id[val]] is False)):
                explored_lst, visited_lst = self._top_sort(val, explored_lst, visited_lst)
                
        if explored_lst[self.graph_id[cur_key]] is False:
            self.top_arr[self.idx] = cur_key
            explored_lst[self.graph_id[cur_key]] = True
            self.idx -= 1
            
        return explored_lst, visited_lst

if __name__ == '__main__':
    graph = {
        "C" : ["A", "B"],
        "A" : ["D"],
        "B" : ["D"],
        "D" : ["H", "G"],
        "H" : ["J", "I"],
        "G" : ["I"],
        "J" : ["M", "L"],
        "M" : [],
        "L" : [],
        "I" : ["L"],
        "E" : ["A", "D", "F"],
        "F" : ["K", "J"],
        "K" : ["J"],
    }
    
    topsort = Topsort(graph)
    print(topsort.top_sort())