def mergesort_edges(arr):
    if len(arr) == 1: # if only one item is left return it
        return arr
    
    k_arr = [] # sorted array
    mid = len(arr) // 2 #midpoint
    left_arr = arr[:mid] # left array
    right_arr = arr[mid:] # right array
    
    left_arr = mergesort_edges(left_arr) # recursion on left array
    right_arr = mergesort_edges(right_arr) # recursion on right array
    
    i = 0 # index of left array
    j = 0 # index of right array
    
    while i < len(left_arr) and j < len(right_arr): # looping until both left and right index is in bound
        if left_arr[i][2] < right_arr[j][2]: # if left item is less than right item
            k_arr.append(left_arr[i])
            i += 1 # next item
        else: # if right item is less than left item
            k_arr.append(right_arr[j])
            j += 1 # next itme
    
    while i < len(left_arr): # if item left in left array
        k_arr.append(left_arr[i])
        i += 1
        
    
    while j < len(right_arr): # if item left in right array
        k_arr.append(right_arr[j])
        j += 1
        
    return k_arr # return the sorted array


def kruskal(graph):
    edges_lst = []
    graph_id = {key : i for key, i in zip(graph.keys(), range(len(graph)))}
    visited_arr = [0 for i in range(len(graph_id))]
    for key, edges in graph.items():
        edges_lst += [(key, edge[0], edge[1]) for edge in edges 
            if (visited_arr[graph_id[key]] == 0 and visited_arr[graph_id[edge[0]]] == 0)]
        visited_arr[graph_id[key]] = 1
        
    edges_lst = mergesort_edges(edges_lst)
    union_arr = [key for key in graph_id.keys()]
    
    mst = 0
    
    for edges in edges_lst:
        grp_1 = edges[0]
        grp_2 = edges[1]
        while union_arr[graph_id[grp_1]] != grp_1:
            grp_1 = union_arr[graph_id[grp_1]]  
        while union_arr[graph_id[grp_2]] != grp_2:
            grp_2 = union_arr[graph_id[grp_2]]  
            
        if grp_1 != grp_2:
            mst += edges[2]
            if graph_id[grp_1] < graph_id[grp_2]:
                union_arr[graph_id[grp_2]] = grp_1
            else:
                union_arr[graph_id[grp_1]] = grp_2
                
    return mst


if __name__ == '__main__':
    graph = {
    "A": [("B", 5), ("D", 4), ("E", 1)],
    "B": [("A", 5), ("C", 4), ("D", 2)],
    "C": [("B", 4), ("J", 2), ("H", 4), ("I", 1)],
    "D": [("A", 4), ("B", 2), ("E", 2), ("H", 2), ("F", 5), ("G", 11)],
    "E": [("D", 2), ("F", 1), ("A", 1)],
    "F": [("E", 1), ("D", 5), ("G", 7)],
    "G": [("H", 1), ("I", 4), ("D", 11), ("F", 7)],
    "H": [("D", 2), ("G", 1), ("I", 6), ("C", 4)],
    "I": [("G", 4), ("H", 6), ("J", 0), ("C", 1)],
    "J": [("C", 2), ("I", 0)]
    }
    print(kruskal(graph))
    