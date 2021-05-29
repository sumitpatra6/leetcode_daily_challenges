def maxProducts(words):
    hash_set = set([''.join(sorted(w)) for w in words])
    hash_set = sorted(hash_set, key=lambda x: len(x))
    print(hash_set)


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
result = maxProducts(words)
print(words)
