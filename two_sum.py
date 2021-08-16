def twoSum(nums, target):
    from collections import defaultdict
    hash_map = defaultdict(list)
    length = len(nums)
    for i in range(length):
        hash_map[target - nums[i]].append(i)
    print(hash_map)
    for i in range(length):
        current = nums[i]
        if current not in hash_map:
            continue
        for j in hash_map[current]:
            if j != i:
                return [i, j]
    return [None, None]



numbers = [2, 5, 5, 11]
target = 10
result = twoSum(numbers, target)
print(result)