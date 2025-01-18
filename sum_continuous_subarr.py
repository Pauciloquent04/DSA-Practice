'''
Total number of subarray whose sum equals k

Brute force approach
'''

def sum_cont_subarr(nums, k):
	count = 0
	sum = 0
	for num in nums:
		sum += nums
		if 