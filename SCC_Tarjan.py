from Data_structure.Stack_Queue_Deque import Stack
import random


def tarjan(graph):
    ST = Stack()
    iden = 0
    ids = [-1 for i in range(len(graph))]
    graph = {key : [val, i] for key, val, i in zip(graph.keys(), graph.values(), range(len(graph)))}
    scc_eles = []
    scc = 0
    while len(sum(scc_eles, [])) != len(graph):
        start = random.choice(list(graph.keys() - sum(scc_eles, [])))
        if start:
            ST.push(start)
            new_completed, iden, ids, new_scc = _tarjan(graph, start, iden, ids, ST)
            scc += new_scc
            scc_eles += new_completed
    return scc, scc_eles
        
    
def _tarjan(graph, node, iden, ids, ST):
    ids[graph[node][1]] = iden
    scc_eles = []
    scc = 0
    for nxt_node in graph[node][0]:
        if ids[graph[nxt_node][1]] == -1:
            ST.push(nxt_node)
            scc_eles, iden, ids, scc = _tarjan(graph, nxt_node, iden + 1, ids, ST)
        if ids[graph[nxt_node][1]] != -1:
            if nxt_node in ST.items:
                if ids[graph[node][1]] == ids[graph[nxt_node][1]]:
                    popped_item = ST.pop()
                    new_list = [popped_item]
                    while ST.peek():
                        if ids[graph[popped_item][1]] == ids[graph[ST.peek()][1]]:
                            popped_item = ST.pop()
                            new_list.append(popped_item)
                        else:
                            break
                    scc_eles.append(new_list)
                    return scc_eles, iden, ids, scc + 1
                ids[graph[node][1]] = min(ids[graph[node][1]], ids[graph[nxt_node][1]])
                return scc_eles, iden, ids, scc

    scc_eles.append([ST.pop()])
    return scc_eles, iden, ids, scc + 1


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
    print(tarjan(graph))