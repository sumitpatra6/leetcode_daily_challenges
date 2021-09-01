def judgeSquareSum(c):
    visited = {}
    for i in range(c):
        print(visited)
        if (c - i*i) in visited and visited[c - i*i] != i:
            return True
        else:
            visited[i*i] = i
    return False


result = judgeSquareSum(1)
print(result)