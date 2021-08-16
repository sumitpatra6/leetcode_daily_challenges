def minWindow(s, t):
    from collections import Counter
    t_counter = Counter(t)
    l, r  = 0, 0
    length = len(s)
    answer  = ''
    max_length = float('inf')
    for r in range(length):
        if s[r] in t_counter:
            t_counter[s[r]] -= 1
        if max(t_counter.values()) <= 0:
            while l <= r:
                if s[l] in t_counter:
                    t_counter[s[l]] += 1
                    if t_counter[s[l]] > 0:
                        l += 1
                        break
                l += 1

            if max_length >= len(s[l-1:r+1]):
                answer = s[l-1:r+1]
                max_length = len(answer)
    return answer


s1 = "a"
s2 = "a"
result = minWindow(s1, s2)
print(result)