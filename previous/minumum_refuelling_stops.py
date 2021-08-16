def minRefuelStops(target, startFuel, stops):
    length = len(stops)
    solution = [None] * (length + 2)
    stops = [[0, startFuel]] + stops + [[target, 0]]
    print(stops)
    solution[0] = [0,0]
    length = len(stops)
    print(solution)
    for i in range(1, length):
        print(solution)
        min_steps = None
        min_left_over = None
        for j in range(i-1, -1, -1):
            if stops[i][0] - stops[j][0] <= stops[j][1] + solution[j][1]:
                steps = solution[j][0] + 1
                left_over = solution[j][1] + stops[j][1] - (stops[i][0] - stops[j][0])
                if not min_steps:
                    min_steps = steps
                    min_left_over = left_over
                else:
                    if steps == min_steps and min_left_over < left_over:
                        mmin_steps = steps
                        min_left_over = left_over

                    if steps < min_steps:
                        min_steps = steps
                        min_left_over = left_over
                if min_steps:
                    solution[i] = [min_steps, min_left_over]
    print(solution)

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
result = minRefuelStops(target, startFuel, stations)
print(result)
