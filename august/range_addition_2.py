def maxCount(m, n, ops):
    x = m
    y = n
    for op in ops:
        x = min(x, op[0])
        y = min(y, op[1])
    return x*y



m = 3
n = 3
ops = []

result = maxCount(m, n, ops)
print(result)