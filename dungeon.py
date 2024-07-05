from Data_structure.Stack_Queue_Deque import Queue

class Dungeon:
    def __init__(self, dun_mat):
        self.start = None
        self.dun_mat = dun_mat
        self.queue = Queue()
        self.row = len(self.dun_mat)
        self.col = len(self.dun_mat[0])
        
    def _set_start(self, cord):
        self.start = cord
        
    def adj_row_col(self, cord):
        r_c_1 = (cord[0], (cord[1] - 1))
        r_1_c = ((cord[0] - 1), cord[1])
        r_c1 = (cord[0], (cord[1] + 1))
        r1_c = ((cord[0] + 1), cord[1])
        return [r_c_1, r_1_c, r_c1, r1_c] 
    
    def find_shortest_path(self):
        self.queue.enqueue(self.start)
        return self._find_shortest_path([self.start])

    def _find_shortest_path(self, path = []):
        while not self.queue.is_empty():
            cord = self.queue.dequeue()
            new_cords = self.adj_row_col(cord)
            
            for row, col in new_cords:
                if (row, col) not in path:
                    if -1 < row < self.row and -1 < col < self.col:
                        if self.dun_mat[row][col] == "E":
                            return [cord, (row, col)]
                        
                        if self.dun_mat[row][col] == ".":
                            self.queue.enqueue((row, col))
                            path = path + [(row, col)]
                                       
            shortest_path = self._find_shortest_path(path)
            if shortest_path:
                for row,col in new_cords:
                    if -1 < row < self.row and -1 < col < self.col:
                        if shortest_path[0] == (row, col):
                            if cord[0] <= row or cord[1] <= row:
                                return [cord] + shortest_path
                            
                else:
                    return shortest_path
        
    


if __name__ == '__main__':
    dun_matrix = [
        ["S", ".", ".", "#", ".", ".", "."],
        [".", "#", ".", ".", ".", "#", "."],
        [".", "#", ".", ".", ".", ".", "."],
        [".", ".", "#", "#", ".", ".", "."],
        ["#", ".", "#", "E", ".", "#", "."]
    ]
    
    dungeon = Dungeon(dun_matrix)
    dungeon._set_start((0, 0))
    print(dungeon.find_shortest_path())