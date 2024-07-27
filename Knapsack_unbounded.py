def matrix_creation(p, w, target):
    matrix = [[0 for i in range(target + 1)] for i in range(len(p) + 1)]
    for i in range(len(matrix)):
        if i == 0:
            continue
        for j in range(target + 1):
            if j - w[i - 1] < 0:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - w[i - 1]] + p[i - 1])

    return matrix


def knapsack_unbounded(p, w, target):
    matrix = matrix_creation(p, w, target)
      
    print(matrix)
    k = target  
    total_weight = 0  
    selected_items = []    
    v = len(matrix) - 1
    while v > 0:
        weight = total_weight + w[v - 1]
        if weight <= target:
                total_weight += w[v - 1]
                selected_items.append(p[v - 1])
        else:
            k -= w[v - 1]
            v -= 1
            
    return selected_items, f"Total cost: {sum(selected_items)}$"
            


if __name__ == '__main__':
    # below arrays are sorted according to cost
    p = [1, 4, 7, 10] # cost of each bag
    w = [1, 2, 3, 5] # weight of each bag
    print(knapsack_unbounded(p, w, 12))