def customSortString(order, s):
    order_map = {}
    for i in range(len(order)):
        order_map[order[i]] = i

    lis = sorted(s, key = lambda x: order_map.get(x, float('inf')))
    # print(lis)
    return ''.join(lis)


order = "cba"
s = "abcd"
result = customSortString(order, s)
print(result)