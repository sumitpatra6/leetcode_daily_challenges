def subsetWithDup(nums):
    size = len(nums)
    set_size = pow(2, size)
    power_set = set()
    for i in range(set_size):
        this_one = []
        for j in range(size):
            if (i & (1 << j)) > 0:
                this_one.append(nums[j])
        power_set.add(tuple(this_one))

    return [list(x) for x in power_set]


numbers =  [1,2,2]
result = subsetWithDup(numbers)
print(result)
