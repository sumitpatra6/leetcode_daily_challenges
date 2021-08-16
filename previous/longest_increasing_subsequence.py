def lengthOfLisIterative(nums):
    lis = [1]*len(nums)
    length = len(nums)
    for i in range(1, length):
        for j in range(i):
            if nums[j] < nums[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)   


def lengthOfLisDynamic(nums):
    b = sorted(list(set(nums)))
    m = len(nums)
    n = len(b)
    matrix = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j  in range(1, n+ 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif nums[i-1] == b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]
nums =[10,9,2,5,3,7,101,18]
result = lengthOfLisIterative(nums)
print(result)
result = lengthOfLisDynamic(nums)
print(result)