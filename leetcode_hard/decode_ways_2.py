def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    memory = {}
    def util(string):
        if not string:
            return 1
        if string[0] == '0':
            return 0
        if string in memory:
            return  string[memory]
        if string[0] == '*':
            count = 0
            for i in range(1, 10):
                _string = str(i) + string[1:]
                left = util(_string[1:])
                count += left
            memory[string] = count
        elif len(string) >= 2 and string[1] == '*':
            count = 0
            for i in range(1, 10):
                _string = string[:1] + str(i) + string[2:]
                left = util(_string[1:])
                right = 0
                if len(_string) >= 2 and int(_string[:2]) <= 26:
                    right = util(_string[2:])
                count += left + right
            memory[string] = count
        else:
            left = util(string[1:])
            right = 0
            if len(string) >= 2 and int(string[:2]) <= 26:
                right = util(string[2:])
            memory[string] = left + right
        return memory[string]
    return util(s)


result = numDecodings('2*')
print(result)