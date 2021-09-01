from pprint import pprint
def calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    solution = [[0]*n for _ in range(m)]
    solution[-1][-1] = 1
    for i in range(n-2, -1, -1):
        solution[-1][i] = solution[-1][i+1] - dungeon[-1][i+1]
    for i in range(m-2, -1, -1):
        solution[i][-1] = solution[i+1][-1] - dungeon[i+1][-1]

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            op1 = solution[i][j+1] - dungeon[i][j+1]
            op2 = solution[i+1][j] - dungeon[i+1][j]
            if op1 >= 0 and op2 >= 0:
                _t = min(op1, op2)
            else:
                _t = max(op1, op2)
            solution[i][j] = _t

    for s in solution:
        print(s)
    return solution[0][0] - dungeon[0][0]
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
result = calculateMinimumHP(dungeon)
print(result)