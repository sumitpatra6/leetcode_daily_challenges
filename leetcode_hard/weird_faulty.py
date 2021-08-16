from typing import List
def game(p: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    total = 0
    length = len(array)
    for i in range(length):
        total += 1 if array[i] == 1 else -1
    print(total)
    alex = 0
    for j in range(length):
        if alex > total - alex:
            return  j
        alex += -1 if p[j] == 0 else 1
    return -1

array = [0,1,0,1]
result = game(array)
print(result)