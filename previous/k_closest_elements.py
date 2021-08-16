from bisect import bisect_left


def findClosestElements(arr, k, x):
    index = bisect_left(arr, x, 0, len(arr))
    l = index
    r = l + 1
    result = []
    while k:
        k -=1
        if l < 0:
            result.append(arr[r])
            r += 1
        elif r >= len(arr):
            result.append(arr[l])
            l -= 1
        elif abs(arr[l] - x) <=   abs(arr[r] - x):
            result.append(arr[l])
            l -= 1
        else:
            result.append(arr[r])
            r += 1
    return sorted(result)


array = [0,0,1,2,3,3,4,7,7,8]
k = 3
x = 5
result = findClosestElements(array, k, x)
print(result)