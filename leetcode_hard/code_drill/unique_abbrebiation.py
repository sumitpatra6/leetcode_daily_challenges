from pprint import pprint
def getMapping(words):
    from collections import defaultdict
    map_dict = defaultdict(set)
    deleted_keys = set()
    for w in words:
        length = len(w)
        for i in range(1, length - 1):
            key = w[:i] + str(length - 1 - i) + w[-1]
            if len(key) >= length or key in deleted_keys:
                continue
            if key in map_dict and w not in map_dict[key]:
                # this means that this key is not acceptable
                del map_dict[key]
                deleted_keys.add(key)
                continue
            map_dict[key].add(w)
    
    pprint(map_dict)
    result_dict = {}
    for key, value in map_dict.items():
        value = list(value)[0]
        print(key, value)
        if value not in result_dict:
            result_dict[value] = key
            continue
            
        if len(result_dict[value]) > len(key):
            result_dict[value] = key
    return list(result_dict.values())


words = ["izzzzzzl","iabczzzl","iabcyyyl"]
result = getMapping(words)
pprint(result)