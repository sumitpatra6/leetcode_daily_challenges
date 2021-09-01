def rectangleArea(rectangles):
    cell_set = set()
    for x1, y1, x2, y2 in rectangles:
        print(x1,y1, x2, y2)
        rows = x2 - x1
        cols = y2 - y1
        for i in range(rows):
            for j in range(cols):
                print(i, j)
                cell_set.add((x1 + i, y1 + j))
        # print(cell_set)
    return len(cell_set)


r = [[0,0,1000000000,1000000000]]
result = rectangleArea(r)
print(result)