def minFlipsMonoIncr(S):
    P = [0]
    for x in S:
        P.append(P[-1] + int(x))

    return min(P[j] + len(S)-j-(P[-1]-P[j])
                for j in range(len(P)))
        




string = "00110"
result = minFlipsMonoIncr(string)
print(result)