import numpy as np

def solveSudoku(board):
    def isSafe(grid, x, y, number):
        # first check he row
        if grid[x][y] != '.':
            return False
        for i in range(9):
            if  number == grid[x][i]:
                return False
        # check the column
        for i in range(9):
            if number == grid[i][y]:
                return False
        # check the sub matrix
        startRow = x - x % 3
        startCol = y - y % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == number:
                    return False
        return True
    answer = []
    def solve():
        nonlocal  answer
        # input("Continue")
        for i in range(9):
            for j in range(9):
                if i == 8 and j == 8 and board[i][j] != '.':
                    return True
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if isSafe(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if i == 8 and j == 8:
                            return True
                        result = solve()
                        if result:
                            return True
                        board[i][j] = '.'
                return

    # print(board)
    # print(isSafe(board, 1, 1, '2'))
    solve()
    return  board


inp = [["5","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]
print(np.matrix(inp))
result = solveSudoku(inp)
print(np.matrix(result))