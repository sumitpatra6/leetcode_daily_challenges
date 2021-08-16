from heapq import heappush, heappop


def nthUglyNumberheap(n: int):
    numbers = []
    heappush(numbers, 1)
    visited = set()
    visited.add(1)
    count = 0
    answer = 1
    while count < n:
        # print(numbers)
        current = heappop(numbers)
        answer = current
        # print(current)
        for i in (2, 3, 5):
            if current * i not in visited:
                visited.add(current * i)
                heappush(numbers, current * i)
        count += 1
    return answer


result = nthUglyNumberheap(1000000000)
print(result)
