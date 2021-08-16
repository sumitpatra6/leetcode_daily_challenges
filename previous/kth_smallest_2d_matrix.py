from typing import List
from bisect import bisect_right
def kthSmallest(matrix, k):
	m = len(matrix) 
	n = len(matrix[0])
	l = matrix[0][0]
	r = matrix[m-1][n-1]
	check = lambda x: sum(bisect_right(row, x) for row in matrix)
	while l < r:
		mid = (l + r) // 2
		# count the number of elements lesser than mid
		if check(mid) >= k:
			r = mid
		else:
			l = mid + 1
	return l
matrix = [[1,2],[1,3]]

k = 2

result = kthSmallest(matrix, k)
print(result)