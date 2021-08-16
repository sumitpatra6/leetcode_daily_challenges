def maximumUniqueSubarray(nums):
    stack = []
    max_total = float('-inf')
    for n in nums:
        print(n, stack)
        if n in stack:
            print(n, stack)
            max_total = max(max_total, sum(stack))
            i = 0
            while stack and stack[0] != n:
                stack.pop(0)
            if stack:
                stack.pop(0)
        stack.append(n)
    max_total = max(max_total, sum(stack))
    return max_total





array = [4,2,4,5,6]
result = maximumUniqueSubarray(array)
print(result)
