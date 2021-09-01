def isValidSerialization(preorder):
    if not preorder:
        return False
    preorder_array = preorder.split(',')
    stack = []
    for p in preorder_array:
        if stack and stack[0] == '#':
            return False
        stack.append(p)
        while stack and stack[-2:] == ['#', '#']:
            # print(stack)
            stack.pop()
            stack.pop()
            if stack:
                stack.pop()
                stack.append('#')
    print(stack)
    if len(stack) == 1 and stack[0] == '#':
        return True
    return False



result = isValidSerialization("#")
print(result)
