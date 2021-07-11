def stoneGame(stones):
    sum_alice = 0
    sum_bob = 0
    step = 0
    while stones:
        t1 = sum(stones[1:])
        t2 = sum(stones[:-1])
        if step == 0:
            if t1 > t2:
                sum_alice += t1
                stones = stones[1:]
            else:
                sum_alice += t2
                stones = stones[:-1]
        else:
            if t1 > t2:
                sum_bob += t2
                stones = stones[:-1]
            else:
                sum_bob += t1
                stones = stones[1:]
        step = int(not step)
    print(sum_alice, sum_bob)
    return abs(sum_alice - sum_bob)
            

stones = [5,3,1,4,2]
result = stoneGame(stones)
print(result)

