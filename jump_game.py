def maxResult(nums, k):
    if not nums:
        return 0
    length = len(nums)
    solution = [0]*length
    # solution[0] = nums[0]
    for i in range(1, length):
        maximum = float('-inf')
        end = -1 if i - k - 1< 0 else i - k -1
        for j in range(i-1, end, -1):
            maximum = max(maximum, solution[j] + nums[j])
        solution[i] = maximum
    print(nums)
    print(solution)
    return solution[-1] + nums[-1]


array =  [1,-5,-20,4,-1,3,-6,-3]
k = 2
result = maxResult(array, k)
print(result)
