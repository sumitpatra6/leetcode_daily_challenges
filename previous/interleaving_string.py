def isInterleave(s1, s2, s3):
    from functools import lru_cache
    original_word = s3
    @lru_cache
    def util(s1, s2, s3, word):
        print(s1, s2,s3, word)
        if s1 == ''  and s2 == ''  and word == original_word:
            return True
        if not s3:
            return False
        r1 = False
        r2 = False
        if s1 and s1[0] == s3[0]:
            r1 = util(s1[1:], s2, s3[1:], word + s1[0])
        if s2 and s2[0] == s3[0]:
            r2 = util(s1, s2[1:], s3[1:], word + s2[0])
        return r1 or r2
    return util(s1, s2, s3, '')

s1 = 'a'
s2 = 'b'
s3 = 'a'
result = isInterleave(s1, s2, s3)
print(result)
