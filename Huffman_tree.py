from Data_structure.priority_queue_graph import Priority_Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Huffman:
    def __init__(self, s):
        self.root = None
        self.table = self.__create_table(s)
        self.PQ = Priority_Queue()
        
    def __create_table(self, s):
        table = {}
        for ele in s:
            if ele not in table.keys():
                table[ele] = 1
            else:
                table[ele] += 1
                
        return table
    
    def create_tree(self):
        for key, count in self.table.items():
            self.PQ.enqueue((Node(key), count))
        
        while not self.PQ.is_empty():
            if self.PQ.size() == 1:
                self.root = self.PQ.dequeue()[0]
                return
                
            left_child = self.PQ.dequeue()
            right_child = self.PQ.dequeue()
            parent = Node(left_child[1] + right_child[1])
            parent.left = left_child[0]
            parent.right = right_child[0]
            self.PQ.enqueue((parent, left_child[1] + right_child[1]))
            
    def create_encode_t(self):
        if not self.root:
            print("Huffman Tree not found")
            return
        self.encode_table = {}
        return self._create_encode_t(self.root, "")
    
    def _create_encode_t(self, node, encoded_str):
        if node.left:
            self._create_encode_t(node.left, encoded_str + "0")
        if node.right:
            self._create_encode_t(node.right, encoded_str + "1")
            
        if not node.left and not node.right:
            self.encode_table[node.val] = encoded_str
            
    def encode(self, s):
        encode = ""
        for val in s:
            if val not in self.encode_table.keys():
                return "Decoding error"
            encode += self.encode_table[val] 
        return encode
        
    def decode(self, s):
        idx = 0
        decoded_str = ""
        while idx < len(s):
            decoded_val, idx = self._decode(self.root, s, idx)
            if decoded_val == "Encoding error":
                return decoded_val
            decoded_str += decoded_val
            
        return decoded_str
                
    def _decode(self, node, s, idx):
        if not node.left and not node.right:
            return node.val, idx
        
        if node is None or idx >= len(s):
            return "Encoding error", idx
        
        val = s[idx]
        
        if val == "0":
            return self._decode(node.left, s, idx + 1)
        else:
            return self._decode(node.right, s, idx + 1)
    
    
if __name__ == '__main__':
    s = "aaabbaaaabccaadabaeaff"
    s1 = "11101101111110110100101100101011100111000000"
    huffman = Huffman(s)
    huffman.create_tree()
    huffman.create_encode_t()
    print(huffman.encode(s))
    print(huffman.decode(s1))

