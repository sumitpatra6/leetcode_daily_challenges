from typing_extensions import TypeAlias


def canReorderDoubled(arr):
    from collections import Counter
    count = Counter(arr)
    for key in sorted(count, key=abs):
        if count[key] > count[2*key]:
            return False
        count[2*key] -= count[key]
    return True

array = [1,2,1,-8,8,-4,4,-4,2,-2]
result = canReorderDoubled(array)
print(result)


# array = [1,2,4,16,8,4]
# result = canReorderDoubled(array)
# print(result)