class NumArray:
    def __init__(self, nums) -> None:
        self.array = nums
        self.n = len(self.array)
        self.bit = [0]*(self.n + 1)
        for i in range(self.n):
            self.initialize(i, self.array[i])

    def initialize(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & (-i)

    def update(self, index, value):
        diff = value - self.array[index]
        self.array[index] = value
        self.initialize(index, diff)

    def getSum(self, index):
        
        sum = 0
        index += 1
        while index > 0:
            sum += self.bit[index]
            index -= index & (-index)
        return sum

    def sumRange(self, left, right):
        return self.getSum(right) - self.getSum(left - 1)





array = [1, 3, 5]

num_obj = NumArray(array)
print(num_obj.sumRange(0, 2))
print(num_obj.update(1, 2))
print(num_obj.sumRange(0, 2))