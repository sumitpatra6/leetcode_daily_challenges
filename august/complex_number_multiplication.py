def complexNumberMultiply(num1, num2):
    if not num1:
        return num2
    if not num2:
        return num1
    num1_array = num1.split('+')
    num2_array = num2.split('+')
    real_array = []
    imaginary_array = []

    def check_type(number):
        """
        1 means imaginary
        0 means real number
        """
        if number.find("i") != -1:
            return 1
        return 0

    def multiply(n1, n2):
        """
        1. If both the numbers are real
        2. If one is real and another is imaginary
        3. If both the numbers are imaginary
        """
        type_1 = check_type(n1)
        type_2 = check_type(n2)
        if type_2 == 1 and type_1 == 1:
            # both imaginary numbers
            return str(int(''.join(list(n1)[:-1])) * int(''.join(list(n2)[:-1])) * -1)
        if type_2 == 0 and type_1 == 0:
            return str(int(n1) * int(n2))
        if type_1 == 1 and type_2 == 0:
            return str(int(n2) * int(''.join(list(n1)[:-1]))) + "i"
        if type_2 == 1 and type_1 == 0:
            return str(int(n1) * int(''.join(list(n2)[:-1]))) + "i"
    # print(multiply("2i", "-2"))
    for i in range(len(num1_array)):
        for j in range(len(num2_array)):
            mul = multiply(num1_array[i], num2_array[j])
            if check_type(mul) == 0:
                real_array.append(int(mul))
            else:
                imaginary_array.append(int(''.join(list(mul)[:-1])))
    return str(sum(real_array)) +"+"+ str(sum(imaginary_array)) + "i"

num1 = "1+-1i"
num2 = "1+-1i"
result = complexNumberMultiply(num1, num2)
print(result)