def longestStrChain(words):
    from collections import defaultdict
    words.sort(key = lambda x: len(x))
    print(words)
    hash_map = defaultdict(set)
    for w in words:
        l = len(w)
        hash_map[l].add(w)
    print(hash_map)
    mamory = {}
    def traverse(word, hash_map, count):
        length = len(word)
        tmp_ans = float('-inf')
        if not word in hash_map[length]:
            return count
        count += 1
        for i in range(length):
            new_w = word[:i] + word[i+1:]
            tmp_ans = max(tmp_ans, traverse(new_w, hash_map, count))
        return tmp_ans
    ans = float('-inf')
    for j in range(len(words) - 1, -1, -1):
        # print("-")
        ans = max(ans, traverse(words[j], hash_map, 0))
    print(ans)
    return ans

# words = ["a","b","ba","bca","bdca","bda"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
longestStrChain(words)