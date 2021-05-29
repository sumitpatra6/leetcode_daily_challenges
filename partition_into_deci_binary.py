def minPartitions(n):
    max_number = 0
    for i in n:
        max_number = max(max_number, int(i))
    return max_number



number = "82734"
result = minPartitions(number)
print(result)
