import time


def removeBoxes(boxes):
    memory = {}

    def util(array):
        nonlocal memory
        # print(array, weight)
        if not array:
            return 0
        key = ''.join(list(map(str, array)))
        if key in memory:
            return memory[key]
        length = len(array)
        answer = float('-inf')
        for i in range(length):
            start = i + 1
            while start < length and array[start] == array[i]:
                start += 1
            w = pow(start - i, 2) + util(array[:i] + array[start:])
            answer = max(answer, w)
        memory[key] = answer
        return answer

    a = util(boxes)
    return a


r = removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
print(r)
print("*************************************************")
t1 = time.time()
result = removeBoxes(
    [1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2,
     2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1,
     1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1])
print(result)

print(time.time() - t1)
