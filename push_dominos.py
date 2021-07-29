def pushDominoes(dominoes):
    length = len(dominoes)
    l = [None]*length # looks like [(0, L), (1, L)]
    r = [None]*length
    def dfs(index, direction, previous='.', time=0):
        if index < 0 or index >= length:
            return
        if dominoes[index] == '.':
            if previous == 'L':
                l[index] = (time+1, 'L')
                dfs(index + direction, direction, 'L', time + 1) 
            else:
                l[index] = (0, '.')
                dfs(index + direction, direction, '.', 0)
        if dominoes[index] == 'L':
            l[index] = (0, 'L')
            dfs(index + direction

    # populate l
    dfs(length - 1, -1)
    # poppulate r
    dfs(0, 1)
    print(l)
    print(r)

string = ".L.R...LR..L.."
result = pushDominoes(string)
