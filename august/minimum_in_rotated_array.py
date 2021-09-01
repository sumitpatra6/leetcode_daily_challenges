def findMin(nums):
    answer = None
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= nums[-1]:
            answer = nums[mid]
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


result = findMin([3,4,5,2])
print(result)