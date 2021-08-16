def largest_island(grid):
    m = len(grid)
    n = len(grid[0])
    maximum = float('-inf')
    memory = {}
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    def dfs(x, y):
        visited = [(x, y)]
        stack = [(x, y)]
        while stack:
            current_x, current_y = stack.pop()
            for d in directions:
                _x = current_x + d[0]
                _y = current_y + d[1]
                if _x < 0 or _x >= m or _y < 0 or _y >= n or (_x, _y) in visited or grid[_x][_y] == 0:
                    continue
                stack.append((_x, _y))
                visited.append((_x, _y))

        return len(visited)


    zero_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                visited = []
                grid[i][j] = 1
                zero_count += 1
                r = dfs(i, j)
                maximum = max(maximum, r)
                grid[i][j] = 0
    if zero_count == 0:
        return m*n

    return maximum


def largest_island_optimized(grid):
    print("---")
    N = len(grid)
    def neighbours(r, c):
        for nr, nc in ((-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc
    
    def dfs(x, y, index):
        grid[x][y] = index
        ans = 1
        for r, c in neighbours(x, y):
            if grid[r][c] == 1:
                ans += dfs(r, c, index)
        return ans
    area = {}
    index = 2
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                area[index] = dfs(i, j, index)
                index += 1
    ans = max(area.values() or [0])
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                seen = {grid[nr][nc] for nr, nc in neighbours(i, j) if grid[i][j] > 1}
                ans = max(ans, 1 + sum([area[k] for k in seen]))
    return ans

grid = [[1,1],[1,0]]
result = largest_island_optimized(grid)
print(result)