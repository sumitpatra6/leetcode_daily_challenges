def maxAreofIsLand(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[0]*n for _ in range(m)]
    print(visited)
    from collections import deque
    movements = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    def check_if_valid(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        area = 0
        while q:
            length = len(q)
            for i in range(length):
                current = q.popleft()
                visited[current[0]][current[1]] = 1
                area += 1
                for x, y in movements:
                    _i = current[0] + x
                    _j = current[1] + y
                    if check_if_valid(_i, _j) and visited[_i][_j] == 0 and grid[_i][_j] == 1:
                        q.append((_i, _j))
        return area

    result = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and grid[i][j] == 1:
                result = max(result,bfs(i, j))
    return result



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
result = maxAreofIsLand(grid)
print(result)
