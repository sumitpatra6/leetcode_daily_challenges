def max_presentations(starts, durations) -> int:
    length = len(starts)
    jobs = []
    for i in range(length):
        jobs.append([starts[i], starts[i] + duration[i]])
    print(jobs)
    jobs.sort(key=lambda x: x[1])
    print(jobs)
    k = 0
    count = 1
    for i in range(1, length):
        if jobs[i][0] >= jobs[k][1]:
            count += 1
            k = i
    return count

starts = [1, 3, 3, 5, 7]
duration = [2, 2, 1, 2, 1]
result = max_presentations(starts, duration)
print(result)