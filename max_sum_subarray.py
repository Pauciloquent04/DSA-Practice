'''
Maximum sum of subarray from array

Brute force approach by me.
'''

def max_sum_subarray(arr):
	sum = float("-inf")
	for i in range(len(arr)):
		temp = 0
		for j in range(i, len(arr)):
			temp += arr[j]
			if temp > sum:
				sum = temp
	return sum


print(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

'''
Learned that Kadane's Algorithm is the optimised 
solution for this type of problems.

At each position, we make a choice:
- Continue previous subarray (current_sum + num)
OR
- Start new subarray from current position (num)

Optimised approach (Kadane's)
'''

def kadane_max_subarray(arr):
	current_sum = max_sum = arr[0]
	for i in arr[1:]:
		current_sum = max(i, current_sum + i)
		max_sum = max(max_sum, current_sum)
	return max_sum
print(kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

'''
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Step by step:
Position  Number  Current_Sum  Max_Sum   Decision
0         -2      -2          -2        Start here
1          1       1           1        Start new
2         -3      -2           1        Continue
3          4       4           4        Start new
4         -1       3           4        Continue
5          2       5           5        Continue
6          1       6           6        Continue
7         -5       1           6        Continue
8          4       5           6        Continue
'''