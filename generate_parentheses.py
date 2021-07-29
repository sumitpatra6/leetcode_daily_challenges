def generateParenthessis(n):
    p = [['()']]
    for i in range(1, n):
        tmp = set()
        previous_list = list(p)[i-1]
        for pr in previous_list:
            for j in range(len(pr)):
                if pr[j] == ')':
                    print('Here')
                    tmp.add(pr[:j] + '()' + pr[j:])
            tmp.add('()' + pr)
        
        p.append(tmp)
    print(p)
    return list(p[-1])


n = 4
#answer = ["((()))","(()())","(())()","()(())","()()()"]
#answer = {'((()))','(()())','(())()','()()()','()(())'}
result = generateParenthessis(n)
print(result)