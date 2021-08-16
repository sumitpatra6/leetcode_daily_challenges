class MapSum:
    def __init__(self):
        self.memory = {}
        self.sum_memory = {}

    def insert(self, key, val):
        current_val = val
        for i in range(len(key)+1):
            prefix = key[:i]
            _substract = self.memory.get(key, 0)
            if prefix in self.sum_memory:
                self.sum_memory[prefix] -= _substract
            self.sum_memory[prefix] = self.sum_memory.get(prefix, 0) + current_val
        self.memory[key] = val
        print(self.memory)
        print(self.sum_memory)

    def sum(self, prefix):
        return self.sum_memory.get(prefix, 0)


mapSum =  MapSum()
mapSum.insert('apple', 3)
print(mapSum.sum('ap'))
mapSum.insert('app', 2)
print(mapSum.sum('ap'))
