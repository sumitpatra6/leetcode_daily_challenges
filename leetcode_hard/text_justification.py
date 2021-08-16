def fullJustify(words, maxWidth):
    answer = []
    current_list = []
    current_length = 0
    length = len(words)
    def adjust(word_list, total_length):
        print(word_list)
        spaces_to_adjust = maxWidth - total_length
        if len(word_list) == 1:
            return word_list[0] + ' '*(maxWidth-total_length)
        factor = spaces_to_adjust // (len(word_list) - 1)
        spaces = ' '*factor
        return spaces.join(word_list)

    for i in range(length):
        if current_length + len(current_list)  + len(words[i]) > maxWidth:
            #adjust the current string with spaces
            r = adjust(current_list, current_length)
            answer.append(r)
            current_list = []
            current_length = 0
        current_list.append(words[i])
        current_length += len(words[i])
        if i == length - 1:
            r = ' '.join(current_list)
            left_spaces = maxWidth - len(r)
            r += ' '*left_spaces
            answer.append(r)
    return answer



words =  ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
result = fullJustify(words, maxWidth)
print(result)