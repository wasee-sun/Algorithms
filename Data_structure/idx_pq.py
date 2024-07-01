from Data_structure.heap_tree_ipq import Min_Heap

class Idx_Priority_Queue:
    def __init__(self, graph):
        self.queue = Min_Heap(graph)
        
    def enqueue(self, ele):
        self.queue.insert(ele)
        
    def dequeue(self):
        return self.queue.extract_min()
        
    def peek(self):
        return self.queue.get_min()
        
    def is_empty(self):
        return len(self.queue.heap) == 0