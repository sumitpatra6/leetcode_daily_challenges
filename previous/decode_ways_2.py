def numDecodings(s):
    if not s:
        return 0
    current = s[0]
    if current == '0':
        return 0
    w = 1 + numDecodings(s[1:])
    wo = 0
    if len(s) > 1:
        current_1 = s[1:]
inp = "11106"
result = numDecodings(inp)