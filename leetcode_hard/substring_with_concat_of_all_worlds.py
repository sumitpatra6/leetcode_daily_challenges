def findSubString(s, words):
    word_map = {}
    for w in words:
        if w not in word_map:
            word_map[w] = 0
        word_map[w] += 1
    
    w_length = len(words[0])
    total_length = w_length * len(words)
    answer = []
    for i in range(len(s) - total_length + 1):
        curren_word_map = {}
        index = 0
        j = 0
        current = s[i:i+total_length]
        for index in range(len(words)):
            part = current[j:j+w_length]
            if part not in curren_word_map:
                curren_word_map[part] = 1
            else:
                curren_word_map[part] += 1
            index += 1
            j += w_length
        if curren_word_map == word_map:
            answer.append(i)
    return answer




string = 'barfoothefoobarman'
words = ['foo', 'bar']
result = findSubString(string, words)
print(result)