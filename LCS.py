def lcs(st1, st2):
    matrix = [[0 for i in range(len(st1) + 1)] for i in range(len(st2) + 1)]
    
    for i in range(len(st2) + 1):
        if i == 0:
            continue
        for j in range(len(st1) + 1):
            if j == 0:
                continue
            if st2[i - 1] == st1[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
                
    return matrix[-1][-1]
    
    
if __name__ == '__main__':
    st1 = "AGGTAB"
    st2 = "GXTXAYB"
    print(lcs(st1, st2))