from collections import defaultdict
def isValidSudoku(board):
    row_map = defaultdict(list)
    column_map = defaultdict(list)
    square_map = defaultdict(list)
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                continue
            current = board[i][j]
            if current  in row_map.get(i, []):
                return False
            else:
                row_map[i].append(current)

            if current in column_map.get(j, []):
                return False
            else:
                column_map[j].append(current)

            x = i // 3
            y = j // 3
            key = "{}_{}".format(x, y)
            if current in square_map.get(key, []):
                return False
            else:
                square_map[key].append(current)
    return True


b = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

result = isValidSudoku(b)
print(result)