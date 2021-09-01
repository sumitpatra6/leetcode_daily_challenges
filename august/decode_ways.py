def numDecodings(s):
    if not s or s == '0':
        return 0
    memory = {}
    def util(string):
        if not string:
            return 1
        if string[0] == '0':
            return 0
        if string in memory:
            return memory[string]
        left = util(string[1:])
        right = 0
        if len(string) >= 2 and int(string[:2]) <= 26:
            right = util(string[2:])
        memory[string] = right + left
        return left + right
    return util(s)
"""
123
"""


result = numDecodings('111111111111111111111111111111111111111111111')
# result = numDecodings('12')
print(result)