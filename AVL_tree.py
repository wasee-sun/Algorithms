from Data_structure.Stack_Queue_Deque import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
        self.queue = Queue()
            
    def height_tree(self):
        if self.root is None:
            return 0
        return self._height(self.root, 0)
    
    def _height_tree(self, node, n_height):
        if node == None:
            return 0
        
        left_h = self._height(node.left, n_height)
        right_h = self._height(node.right, n_height)
        
        return max(left_h, right_h) + 1
    
    def find(self, data): #find the node
        if self.root is None:
            print("No root found")
            return
        else:
            return self._find(data, self.root)
        
    def _find(self, data, node):
        if data == node.data:
            return node
        
        elif data < node.data and node.left is not None:
            return self._find(data, node.left)
        
        elif data > node.data and node.right is not None:
            return self._find(data, node.right)
        
        else:
            print("Node not found")
            return
            
    def search(self, data): #find the node
        if self.root is None:
            print("No root found")
            return
        else:
            return self._search(data, self.root)
        
    def _search(self, data, node):
        if data == node.data:
            return True
        
        elif data < node.data and node.left is not None:
            return self._search(data, node.left)
        
        elif data > node.data and node.right is not None:
            return self._search(data, node.right)
        
        return False
    
    def min_node(self):
        if self.root is None:
            print("No root found")
            return
        else:
            self._min_node(self.root)
            
    def _min_node(self, node):
        if node.left:
            return self._min_node(node.left)
        else:
            return node
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
                node.left.parent = node
                self._inspect_insertion(node.left)
                
        elif data > node.data:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data)
                node.right.parent = node
                self._inspect_insertion(node.right)
        
        else:
            print("Value already in tree")
        
    def delete_val(self, data):
        if self.root is None:
            print("No root found")
            return
        else:
            self.delete_node(self.find(data))
            
    def delete_node(self, node):
        
        #if data doesn't exist
        if node == None:
            print("Node to be deleted is not found")
            return
        
        node_child = 0
        if node.left:
            node_child += 1
        if node.right:
            node_child += 1
        
        node_parent = node.parent
        if node_child == 0:
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                elif node_parent.right == node:
                    node_parent.right = None
                    
            else:
                self.root = None
                
        if node_child == 1:
            if node.left:
                child = node.left
            if node.right:
                child = node.right
            
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = child
                elif node_parent.right == node:
                    node_parent.right = child
            
            else:
                self.root = child
                
            child.parent = node_parent
            
        if node_child == 2:
            min_n = self._min_node(node.right)
            node.data = min_n.data
            
            self.delete_node(min_n)
            return
                
        if node_parent != None:
            node_parent.height = max(self.get_height(node_parent.left), 
                                     self.get_height(node_parent.right)) + 1
            
            self._inspect_deletion(node_parent)
            
    def _inspect_insertion(self, cur_node, path = []):
        if cur_node == None:
            return
        
        path = [cur_node] + path
        
        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)
        
        if abs(left_height - right_height) > 1: # unbalanced
            self._rebalance_node(path[0], path[1], path[2]) #node, child, grandchild
            return
        
        new_height = 1 + cur_node.height
        if cur_node.parent != None:
            if new_height > cur_node.parent.height: #adjusting the height of parent node
                cur_node.parent.height = new_height
            
        self._inspect_insertion(cur_node.parent, path)
        
    def _inspect_deletion(self, cur_node):
        if cur_node == None:
            return
        
        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)
        
        if abs(left_height - right_height) > 1: # unbalanced
            child=self.taller_child(cur_node) #find the taller child
            g_child=self.taller_child(child) #find the grandchild
            self._rebalance_node(cur_node, child, g_child) #node, child, grandchild
			
        self._inspect_deletion(cur_node.parent) # recurssive find out untill we hit the root
        
    def _rebalance_node(self, node, child, g_child):
        if node.left == child and child.left == g_child: # left left child
            self._right_rotate(node) # rotate the grandparent
            
        elif node.left == child and child.right == g_child: # left right child
            self._left_rotate(child) # rotate the parent
            self._right_rotate(node) # rotate the grandparent
            
        elif node.right == child and child.right == g_child: # right right child
            self._left_rotate(node) # rotate the grandparent
            
        elif node.right == child and child.left == g_child: # right left child
            self._right_rotate(child) # rotate the parent
            self._left_rotate(node) # rotate the grandparent
            
        else:
            raise Exception("_rebalance_node: node, child, g_child configuration not recognized")
    
    def _left_rotate(self, node):
        node_par = node.parent # parent of the node
        right_child = node.right #get the right child of node
        right_child_left = right_child.left #get the left child of right child
        right_child.left = node # right child left is now node
        node.parent = right_child #now switch the parent of node to right child
        node.right = right_child_left # right child of node will be the left child of the new parent
        if right_child_left != None: # if the left child of the previous node.right is not None
            right_child_left.parent = node #parent of the right child's left child is node now
            
        right_child.parent = node_par #new parent of the right child is the previous parent of node
        if node_par == None: #if there is was no node.parent
            self.root = right_child # root is now the right child
        else:
            if node_par.left == node: # finding which child was node of node.parent
                node_par.left = right_child
            else:
                node_par.right = right_child
        #fixing the height of the changed node and it's previous children
        node.height = max(self.get_height(node.left),
			            self.get_height(node.right)) + 1
        
        right_child.height = max(self.get_height(right_child.left),
                                self.get_height(right_child.right)) + 1
        
    def _right_rotate(self, node):
        node_par = node.parent #parent of the node
        left_child = node.left #left child of the node
        left_child_right = left_child.right #right child of the left child
        left_child.right = node # left child right is now node
        node.parent = left_child # now switch the parent of node to left child
        node.left = left_child_right # left child of right child will be the new left child of node
        if left_child_right != None:
            left_child_right.parent = node #parent of the left child's right child is node now
            
        left_child.parent = node_par # new parent of the left child is the previous parent of node
        if node_par == None: #if there is was no node.parent
            self.root = left_child # root is now the left child
        else:
            if node_par.left == node: # finding which child was node of node.parent
                node_par.left = left_child
            else:
                node_par.right = left_child
                
        #fixing the height of the changed node and it's previous children
        node.height = max(self.get_height(node.left),
			            self.get_height(node.right)) + 1
        
        left_child.height = max(self.get_height(left_child.left),
			                    self.get_height(left_child.right)) + 1
        
    def get_height(self,cur_node):
        if cur_node==None: 
            return 0
        return cur_node.height

    def taller_child(self,cur_node):
        left=self.get_height(cur_node.left)
        right=self.get_height(cur_node.right)
        return cur_node.left if left >= right else cur_node.right
        
    def bfs_traversal(self):
        elements = []
        
        if self.root is None:
            print("No root node found")
            return
        else:
            self.queue.enqueue(self.root)
        
        while not self.queue.is_empty():
            popped_item = self.queue.dequeue()
            elements.append(popped_item.data)
            if popped_item.left and popped_item.right:
                self.queue.enqueue(popped_item.left)
                self.queue.enqueue(popped_item.right)
            elif popped_item.left:
                self.queue.enqueue(popped_item.left)
            elif popped_item.right:
                self.queue.enqueue(popped_item.right)
        
        return elements
            
              
if __name__ == "__main__":
    avl = AVL()
    elements = [10, 6, 18, 2, 8, 17, 1]
    # elements = [6, 3, 8, 2, 4, 5]
    # elements = [10, 5, 18, 2, 6, 15, 20, 14, 17, 16]
    for i in elements:
        avl.insert(i)
    print(avl.bfs_traversal()) 
    avl.delete_val(10)
    print(avl.bfs_traversal()) 
            
    