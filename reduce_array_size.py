def minSetSize(arr):
    from collections import Counter
    number_counter = Counter(arr)
    num_set = set(arr)
    num_set = sorted(num_set, key=lambda x: number_counter[x], reverse=True)
    print(num_set)
    total_count = len(arr)
    count = 0
    set_count = 0
    for n in num_set:
        set_count += 1
        count += number_counter[n]
        if total_count - count <= total_count // 2:
            break
    return set_count





array = [7,7,7,7,7,7,7]
result = minSetSize(array)
print(result)