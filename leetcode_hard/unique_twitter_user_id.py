from heapq import heapify, heappush, heappop


def get_sum(l):
    visited = set()
    length = len(l)
    total = 0

    def get_element(element, existing):
        while element in existing:
            element += 1
        return element

    for i in range(length):
        current = l[i]
        if current in visited:
            current = get_element(current, visited)
        total += current
        visited.add(current)
    return total


result = get_sum([3, 2, 1, 2, 7])
print(result)
