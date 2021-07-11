def palindromePairs(words):
    for x in enumerate(words):
        print(x)
    length_array = [_ for _ in range(len(words))]
    print(length_array)
    from itertools import combinations
    comb = combinations(length_array, 2)
    ret = []
    for c in comb:
        w1 = words[c[0]] + words[c[1]]
        if w1 == w1[::-1]:
            ret.append([c[0], c[1]])
        w2 = words[c[1]] + words[c[0]]
        if w2 == w2[::-1]:
            ret.append([c[1], c[0]])
    print(ret)
    return ret
    
words = ["abcd","dcba","lls","s","sssll"]
palindromePairs(words)
