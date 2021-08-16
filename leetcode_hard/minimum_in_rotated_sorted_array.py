def findMin(nums):
    answer = -1
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == len(nums) - 1 or nums[mid] < nums[-1]:
            hi = mid - 1
            answer = mid
        else:
            lo = mid + 1

    return nums[answer]


array = [2,2,2,0,1]
result = findMin(array)
print(result)