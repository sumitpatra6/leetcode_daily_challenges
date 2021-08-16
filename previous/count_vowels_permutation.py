"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.

a -> e
e -> a, i
i -> a, e, o, u
o -> i u
u -> a
"""


def countVowelPermutation(n):
    from functools import lru_cache
    neighbours = {
        'a' : ['e'],
        'e' : ['a', 'i'],
        'i' : ['a', 'e', 'o', 'u'],
        'o' : ['i', 'u'],
        'u' : ['a']
    }
    count = 0
    @lru_cache
    def dfs(start_node, remaining):
        remaining -= 1
        if not remaining:
            return 1
        count = 0
        for n in neighbours[start_node]:
            count += dfs(n, remaining)
        return count

    for start in neighbours:
        count += dfs(start, n)
    return count


result = countVowelPermutation(5)
print(result)
