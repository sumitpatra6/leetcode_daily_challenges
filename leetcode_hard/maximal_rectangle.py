def maximalRectangle(matrix):
    m = len(matrix)
    n = len(matrix[0])
    answer = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                start_x = i
                start_y = j
                h_count = float('inf')
                c_count = 0
                while start_x < m and matrix[start_x][j] != '0':
                    c = 0
                    while start_y < n and matrix[start_x][start_y] != '0':
                        c += 1
                        start_y += 1
                    h_count = min(c, h_count)
                    start_y = j
                    c_count += 1
                    start_x += 1
                    answer = max(h_count * c_count, answer)
    return answer



matrix =  [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
import numpy as np
print(np.matrix(matrix))
result = maximalRectangle(matrix)
print(result)