class FenTree:
    def __init__(self, array) -> None:
        self.array = [0]*(len(array) + 1)
        self.length = len(array)
        for i in range(len(array)):
            self.update(len(array), i, array[i])

    def update(self, n, i, v):
        i += 1
        while i <= n:
            self.array[i] += v
            i += i&(-i) 
    
    def sum(self, i):
        i += 1
        s = 0 
        while i > 0:
            s += self.array[i]
            i -= i&(-i)
        return s



array = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
f_tree = FenTree(array)
print(f_tree.array)
print(f_tree.sum(2))