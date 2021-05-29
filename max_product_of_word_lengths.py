def maxProducts(words):
    def check(w1, w2):
        w1 = set(w1)
        w2 = set(w2)
        for c in w1:
            if c in w2:
                return False
        return True
    max_result = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = sorted(words[i])
            word2 = sorted(words[j])
            if len(word1) < len(word2):
                if not check(word1, word2):
                    continue
            else:
                if not check(word2, word1):
                    continue
            print(word1, word2)
            max_result = max(max_result, len(word1) * len(word2))
    return max_result






words = ["a","aa", "aaa", "aaaa"]
result = maxProducts(words)
print(result)
