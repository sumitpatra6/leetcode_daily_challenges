def evalRPN(tokens):
    operand_stack = []
    for t in tokens:
        print(t)
        if t.lstrip('-').isalnum():
            operand_stack.append(t)
        else:
            num1 = int(operand_stack.pop())
            num2 = int(operand_stack.pop())
            if t == '+':
                result = num1 + num2
            if t == '-':
                result = num2 - num1
            if t == '*':
                result = num1 * num2
            if t == '/':
                result = num2 // num1
                print(result)
            operand_stack.append(str(result))
        print(operand_stack)
    return int(operand_stack[0])





tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = evalRPN(tokens)
print(result) 
