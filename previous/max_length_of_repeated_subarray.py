from pprint import pprint
def findLength(nums1, nums2):
	"""
	This logic is wrong
	"""
	def util(nums1, nums2, len_till_now):
		if not nums1 or not nums2:
			return len_till_now
		if nums1[0] == nums2[0]:
			return util(nums1[1:], nums2[1:], len_till_now + 1)
		return max(util(nums1[1:], nums2, len_till_now),
		util(nums1, nums2[1:], len_till_now),
		util(nums1[1:], nums2[1:], len_till_now))
	return util(nums1, nums2, 0)


def findLengthDynamic(nums1, nums2):
	m = len(nums1)
	matrix = [[0]*(m+1) for _ in range(m+1)]

	# pprint(matrix)
	for i in range(m-1, -1, -1):
		for j in range(m-1, -1, -1):
			if nums1[i] == nums2[j]:
				matrix[i][j] = matrix[i+1][j+1] + 1
	return max(max(row) for row in matrix)
	

nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1] 
result = findLength(nums1, nums2)
print(result)
