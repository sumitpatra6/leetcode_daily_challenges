def candy(ratings):
    n = len(ratings)
    candies = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    sum = candies[-1]
    for i in range(n -2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
        sum += candies[i]
    return sum


ratings = [1,2,2]
result = candy(ratings)
print(result)