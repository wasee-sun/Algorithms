class Min_Heap:
    def __init__(self, graph):
        self.heap = []  # Initialize an empty heap
        self.ki = {i : j for i, j in zip(graph.keys(), range(len(graph)))}
        self.ps = [-1 for i in range(len(graph))]
        
    def _stifup(self, idx):
        par_idx = (idx -1) // 2  # Calculate the parent index
        if par_idx < 0:
            return
        # If the parent node is greater than the current node, swap them
        if self.heap[par_idx][1] > self.heap[idx][1]:
            self.heap[par_idx], self.heap[idx] = self.heap[idx], self.heap[par_idx]
            self.ps[self.ki[self.heap[par_idx][0]]], self.ps[self.ki[self.heap[idx][0]]] = self.ps[self.ki[self.heap[idx][0]]], self.ps[self.ki[self.heap[par_idx][0]]]
        # Recursively sift up the parent node
        return self._stifup(par_idx)
        
    def _stifdown(self, idx):
        left_idx = (2 * idx) + 1  # Calculate the left child index
        right_idx = (2 * idx) + 2  # Calculate the right child index
        min_idx = None
        
        # If there is no left child, return
        if left_idx >= len(self.heap):
            return
        
        # If there is no right child, the minimum index is the left child index
        if right_idx >= len(self.heap):
            min_idx = left_idx
        else:
            # Otherwise, the minimum index is the index of the smaller child
            if self.heap[left_idx][1] < self.heap[right_idx][1]:
                min_idx = left_idx
            else:
                min_idx = right_idx
                
        # If the current node is greater than the minimum child, swap them
        if self.heap[idx][1] > self.heap[min_idx][1]:
            self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
            self.ps[self.ki[self.heap[min_idx][0]]], self.ps[self.ki[self.heap[idx][0]]] = self.ps[self.ki[self.heap[idx][0]]], self.ps[self.ki[self.heap[min_idx][0]]]
        # Recursively sift down the minimum child
        return self._stifdown(min_idx)
        
    def insert(self, val):
        if self.ps[self.ki[val[0]]] != -1:
            old_val = self.heap[self.ps[self.ki[val[0]]]]
            idx = self.ps[self.ki[val[0]]]
            self.heap[self.ps[self.ki[val[0]]]] = val
            if val[1] < old_val[1]:
                self._stifup(idx)
            else:
                self._stifdown(idx)
        else:
            self.heap.append(val) # Insert the value at the end of the heap
            self.ps[self.ki[val[0]]] = len(self.heap) - 1
            self._stifup(len(self.heap) - 1)  # Sift up the inserted value
        
    def get_min(self):
        return self.heap[0]  # Return the minimum value (root of the heap)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]  # Store the minimum value
        self.heap[0] = self.heap[-1]  # Replace the root with the last value in the heap
        self.ps[self.ki[min_val[0]]] = -1
        if self.ps[self.ki[self.heap[0][0]]] != -1:
            self.ps[self.ki[self.heap[0][0]]] = 0
        self.heap.pop()# Remove the last value (now at the root)
        self._stifdown(0)  # Sift down the root value
        return min_val  # Return the minimum value
        
