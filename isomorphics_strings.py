def isIsoMorphic(s, t):
    mapping_s_t = {}
    mapping_t_s = {}
    for cs, ct in zip(s, t):
        if cs not in mapping_s_t and ct not in mapping_t_s:
            mapping_s_t[cs] = ct
            mapping_t_s[ct] = cs
        elif mapping_s_t.get(cs) != ct or mapping_t_s.get(ct) != cs:
            return False
    return True
s1 = 'paper'
s2 = 'title'

result = isIsoMorphic(s1, s2)
print(result)