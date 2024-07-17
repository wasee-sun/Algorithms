import numpy as np


def coin_change(c, target):
    matrix = [np.inf for i in range(target + 1)]
    matrix[0] = 0
    
    for i in range(1, target + 1):
        for coin in c:
            if i - coin < 0:
                continue
            else:
                matrix[i] = min(matrix[i - coin] + 1, matrix[i])
    
    return matrix[target]
            


if __name__ == '__main__':
    # below arrays are sorted according to cost
    coin = [1, 2, 5] # cost of each note
    coin1 = [3, 5, 8] # cost of each note
    coin2 = [2, 5] # cost of each note
    print(coin_change(coin, 11))
    print(coin_change(coin1, 20))
    print(coin_change(coin2, 11))