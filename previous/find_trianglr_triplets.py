def triangle_number(nums):
    from itertools import combinations
    def validity_check(a, b,c):
        if a+b > c and a+ c> b and b+c > a:
            return True
        return False
    combinations = combinations(nums, 3)
    count = 0
    for c in combinations:
        if validity_check(c[0], c[1], c[2]):
            count += 1
    return count


nums = [4,2,3,4]
result = triangle_number(nums)
print(result)

