from Data_structure.heap_tree import Min_Heap

class Priority_Queue:
    def __init__(self):
        self.queue = Min_Heap()
        
    def enqueue(self, ele):
        self.queue.insert(ele)
        
    def dequeue(self):
        return self.queue.extract_min()
        
    def peek(self):
        return self.queue.get_min()
    
    def size(self):
        return len(self.queue.heap)
        
    def is_empty(self):
        return len(self.queue.heap) == 0