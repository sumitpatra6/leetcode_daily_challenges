from pprint import pprint


def setZeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_vector = [False]*m
    col_vector = [False]*n
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                row_vector[row] = True
                col_vector[col] = True

    for row in range(m):
        for col in range(n):
            if row_vector[row] or col_vector[col]:
                matrix[row][col] = 0

    return matrix


result = setZeros([[1,1,1],[1,0,1],[1,1,1]])
pprint(result)