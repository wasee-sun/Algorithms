class Min_Heap:
    def __init__(self):
        self.heap = []  # Initialize an empty heap
        
    def _stifup(self, idx):
        par_idx = (idx -1) // 2  # Calculate the parent index
        if par_idx < 0:
            return
        # If the parent node is greater than the current node, swap them
        if self.heap[par_idx][1] > self.heap[idx][1]:
            self.heap[par_idx], self.heap[idx] = self.heap[idx], self.heap[par_idx]
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
        # Recursively sift down the minimum child
        return self._stifdown(min_idx)
        
    def insert(self, val):
        self.heap.append(val)  # Insert the value at the end of the heap
        self._stifup(len(self.heap) - 1)  # Sift up the inserted value
        
    def get_min(self):
        return self.heap[0]  # Return the minimum value (root of the heap)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]  # Store the minimum value
        self.heap[0] = self.heap[-1]  # Replace the root with the last value in the heap
        self.heap.pop()  # Remove the last value (now at the root)
        self._stifdown(0)  # Sift down the root value
        return min_val  # Return the minimum value
        
        
    