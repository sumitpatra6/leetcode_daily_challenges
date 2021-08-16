def partitionDisjoint(nums):
    length = len(nums)
    left = [float('-inf')]*length
    right = [float('inf')]*length
    left[0] = nums[0]
    right[-1] = nums[-1]
    for i in range(1, length):
        left[i] = max(left[i-1], nums[i])
    for i in range(length -2, -1, -1):
        right[i] = min(right[i+1], nums[i])
    print(nums)
    print(left)
    print(right)
    for i in range(length-1):
        if left[i] < right[i+1]:
            return i+1
    return 0

nums =  [1,1,1,0,6,12]
result = partitionDisjoint(nums)
print(result)
