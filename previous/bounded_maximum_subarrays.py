def numSubarrayBoundedMax(nums, left, right):
    def count(bound):
        ans = 0
        cnt = 0
        for x in nums:
            cnt = cnt + 1 if x <= bound else 0
            ans += cnt
        return ans

    return count(right) - count(left - 1)



nums = [2, 1, 4, 3]
left = 2
right = 3
result = numSubarrayBoundedMax(nums, left, right)
print(result)
