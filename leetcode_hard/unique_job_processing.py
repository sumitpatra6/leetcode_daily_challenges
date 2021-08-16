def process_candidates(s, w, b):
    def util(i, j, current_cost, current_weight):
        pass

    return util(0, 0, 0, 0)


answer = process_candidates([2, 2, 3, 4], [2, 4, 4, 5], 15)
print(answer, 10)

answer = process_candidates([5, 6, 7, 8], [8, 9, 10, 11], 8)
print(answer, 0)

answer = process_candidates([6, 5, 5, 7], [15, 10, 10, 18], 20)
print(answer, 20)

answer = process_candidates([5, 6, 7, 4, 3, 4, 8, 1, 5, 2, 4, 7, 3, 6, 2, 9, 4, 3, 5],
                            [3, 5, 5, 4, 4, 3, 5, 1, 3, 2, 3, 6, 3, 4, 1, 7, 5, 3, 4], 30)
print(answer, 17)
