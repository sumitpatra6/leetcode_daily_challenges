def maximumGap(nums):
    if len(nums) < 2:
        return 0
    nums.sort()
    answer = float('-inf')
    for i in range(1, len(nums)):
        answer = max(answer, nums[i] - nums[i-1])
    print(answer)
    return answer


numbers = [3,6,9,1]
result = maximumGap(numbers)
print(result)
