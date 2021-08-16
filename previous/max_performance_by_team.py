def maxPerformance(n, speed, efficiency, k):
    _speed = [x for x, _ in sorted(zip(speed, efficiency), key=lambda p:p[1])]
    efficiency.sort()
    print(_speed)
    print(efficiency)
    from functools import lru_cache
    @lru_cache
    def util(index, total_speed, min_eff, count):
        if index >= n:
            return total_speed * min_eff
        if count == k:
            return total_speed * min_eff
        r1 = util(index + 1, total_speed + _speed[index], min(min_eff, efficiency[index]), count + 1)
        r2 = util(index + 1, total_speed, min_eff, count)
        return max(r1, r2)
    return util(0, 0, float('inf'), 0)

def maxPerformanceOp(n, speed, efficiency, k):
    from heapq import heappop, heappush
    engineers = list(zip(efficiency, speed))
    engineers.sort(reverse=True)
    min_heap = []
    speedSum = 0
    ans = 0
    for e, s in engineers:
        speedSum += s
        heappush(min_heap, s)
        if len(min_heap) > k:
            speedSum -= heappop(min_heap)
        ans = max(ans, speedSum*e)
    return ans % 1_000_000_007

n = 6
speed =  [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k =4
result = maxPerformanceOp(n, speed, efficiency, k)
print(result)
