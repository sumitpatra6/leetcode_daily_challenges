def threeSumClosest(nums, target):
    nums.sort()
    closest = None
    closest_triplet = None
    length = len(nums)
    for i in range(length):
        j = i + 1
        k = length - 1
        while j < k:
            print(j, k, closest, closest_triplet)
            _sum = nums[i] + nums[j] + nums[k]
            if  closest is None:
                closest = abs(target - _sum)
                closest_triplet = (nums[i], nums[j], nums[k])
            elif abs(target - _sum) < closest:
                closest = abs(target - _sum)
                closest_triplet = (nums[i], nums[j], nums[k])
            
            _sum1 = nums[i] + nums[j+1] + nums[k] 
            _sum2 = nums[i] + nums[j] + nums[k-1]
            if abs(target - _sum1) < abs(target - _sum2):
                j  = j + 1
            else:
                k -= 1
    print(closest, closest_triplet)
    print(sum(closest_triplet))




nums = [-1,-5,-3,-4,2,-2]
target = 0
result = threeSumClosest(nums, target)
