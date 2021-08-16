def trap(height):
    length = len(height)
    left = [0]*length
    right = [0]*length
    left[0] = height[0]
    right[-1] = height[-1]
    for i in range(1, length):
        left[i] = max(left[i-1], height[i])

    for i in range(length -2, -1, -1):
        right[i] = max(right[i+1], height[i])

    total = 0 
    for i in range(length):
        total += min(left[i], right[i]) - height[i]
    return total
height = [4,2,0,3,2,5]
result = trap(height)
print(result)
