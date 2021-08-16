def findPeakElement(nums):
    def util(nums, lo, hi):
        mid = (lo + hi) // 2
        print(mid)
        if hi < lo:
            return None
        l_flag = True
        r_flag = True
        if mid - 1 >= 0 and nums[mid] < nums[mid-1]:
            l_flag = False

        if mid + 1 < len(nums) and nums[mid] < nums[mid+1]:
            r_flag = False
        if r_flag and l_flag:
            return mid
        li = util(nums, lo, mid - 1)
        if li:
            return li
        else:
            return util(nums, mid + 1, hi)

    res = util(nums, 0, len(nums) - 1)
    if not res:
        return 0
    else:
        return res

nums = [1,2]
result = findPeakElement(nums)
print(result)

