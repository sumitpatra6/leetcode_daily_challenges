def is_integer(string):
    if len(string) == 0:
        return False
    if string[0] in '+-':
        string = string[1:]
    if len(string) == 0:
        return False
    for s in string:
        if s not in '0123456789':
            return False
    return True

def is_decimal(string):
    if len(string) == 0:
        return False
    if string[0] in '+-':
        string = string[1:]

    if len(string) == 0:
        return False
    if '-' in string or '+' in string:
        return False
    _index  = string.find('.')
    if _index == -1:
        return is_integer(string)
    else:
        params_1 = string[:_index]
        params_2 = string[_index+1:]
        return (len(params_1) == 0 or is_integer(params_1)) and (is_integer(params_2) or len(params_2) == 0)

def isNumber(string):
    string = string.lower()
    _index = string.find('e')
    if _index == -1:
        return is_decimal(string)
    else:
        p1 = string[:_index]
        p2 = string[_index+1:]
        if not p1 or not p2:
            return False
        return is_decimal(p1) and is_integer(p2)

def test_decimal():
    assert is_decimal('1.23') == True
    assert is_decimal('.123') == True
    assert is_decimal('123.') == True
    assert is_decimal('123') == True
    assert is_decimal('123e') == False
    print("All decimal tests passed")

def test_integer():
    assert is_integer('123') == True
    assert is_integer('1.23') == False
    assert is_integer('+123') == True
    assert is_integer('++1234') == False
    print("Done. All passes integer check")

def test_valid_number():
    assert isNumber('2') == True
    assert isNumber('0089') == True
    assert isNumber('-0.1') == True
    assert isNumber('+3.14') == True
    assert isNumber('4.') == True
    assert isNumber('-.9') == True
    assert isNumber('2e10') == True
    assert isNumber('-90E3') == True
    assert isNumber('3e+7') == True
    assert isNumber('+6e-1') == True
    assert isNumber('53.5e93') == True
    assert isNumber('4.') == True
    assert isNumber('abc') == False
    assert isNumber('1a') == False
    assert isNumber('1e') == False
    assert isNumber('e3') == False
    assert isNumber('99e2.5') == False
    assert isNumber('--6') == False
    assert isNumber('-+3') == False
    assert isNumber('95a54e53') == False
    print("All numbers test done")

if __name__ == '__main__':
    test_integer()
    test_decimal()
    test_valid_number()
