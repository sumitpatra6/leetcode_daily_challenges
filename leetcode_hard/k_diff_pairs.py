from collections import defaultdict
from collections import Counter
from math import factorial
def k_difference(nums, k):
    print(nums)
    answer = 0
    count = Counter(nums)
    print(count)
    visited = set()
    for key in sorted(count):
        current = key
        if current in visited:
            continue
        visited.add(current)
        target = current + k
        if current == target:
            if count[current] == 1:
                continue
            answer += 1
        if current != target and count[target] != 0:
            answer += 1
    return answer

numbers = [1,3,1,5,4]
k = 0
result = k_difference(numbers, k)
print(result)
        
