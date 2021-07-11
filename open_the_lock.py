def openLock(deadends, target):
    from collections import deque
    def neighbours(code):
        for i in range(4):
            x = int(code[i])
            for diff in (1, -1):
                y = (x + diff + 10) % 10
                yield code[:i] + str(y) + code[i+1:]
    deadset = set(deadends)
    if "0000" in deadset:
        return -1
    q = deque(["0000"])
    steps = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == target:
                return steps
            for nei in neighbours(curr):
                if nei in deadset:
                    continue
                deadset.add(nei)
                q.append(nei)
        steps += 1
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = '0202'
result = openLock(deadends, target)
print(result)
deadends = ['8888']
target = '0009'
result = openLock(deadends, target)
print(result)
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
result = openLock(deadends, target)
print(result)
