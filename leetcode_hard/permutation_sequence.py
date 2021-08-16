"""
in each steap
index = k / n
k = k - n + 1
n = n - 1
"""

def getPermutation(n , k):
    from math import factorial
    array = [i for i in range(1, n+1)]
    k = k
    def util(n, k, array, current):

        if k == 1:
            array = list(map(str, array))
            current += ''.join(array)
            return current

        fact = factorial(n-1)
        index = k // fact
        k = k % fact
        if k > 0:
            current += str(array[index])
            return util(n-1, k, array[:index] + array[index+1:], current)
        else:
            return array[index-1] + (array[:index-1] + array[index:])[::-1] 
    return util(n, k, array, '')



result = getPermutation(4, 4)
print(result)