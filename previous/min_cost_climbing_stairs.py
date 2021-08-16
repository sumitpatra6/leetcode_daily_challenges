def minCostClimbingStairs(cost):
    if not cost:
        return 0
    solution = [0]*(len(cost)+1)
    for i in range(2, len(cost) + 1):
        solution[i] = min(solution[i-1] + cost[i-1] , solution[i-2] + cost[i-2])
    print(solution)
    return solution[-1]


array = [1,100,1,1,1,100,1,1,100,1]
result = minCostClimbingStairs(array)
print(result)


