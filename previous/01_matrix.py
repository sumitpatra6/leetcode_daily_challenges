from pprint import pprint
def updateMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    answer = [[float('inf')]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                answer[i][j] = 0
                continue
            if i > 0:
                answer[i][j] = min(answer[i][j], answer[i-1][j] + 1)
            if j > 0:
                answer[i][j] = min(answer[i][j], answer[i][j-1] + 1)

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i < m -1:
                answer[i][j] = min(answer[i][j], answer[i+1][j] + 1)
            if j < n -1:
                answer[i][j] = min(answer[i][j], answer[i][j+1] + 1)
    pprint(answer)
matrix = [[0,0,0],[0,1,0],[1,1,1]]
result = updateMatrix(matrix)
pprint(result)
