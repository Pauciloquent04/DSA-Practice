'''
Rotate array by given k spaces

Brute force approach
'''

def rotate_array(nums, k):
	nums_len = len(nums)
	k = k % nums_len
	rotate = []
	if k == 0:
		return nums
	elif k <= nums_len/2:
		for i in range(k):
			rotate.insert(0, nums.pop())
		nums = rotate + nums
	else:
		for i in range(nums_len - k):
			rotate.insert(0, nums.pop(0))
		nums += rotate
	return nums

nums = []
nums_len = int(input("Enter the length of array: "))
for i in range(nums_len):
	nums.append(int(input(f"Enter element {i+1}: ")))
k = int(input("Enter the number of steps to rotate the array: "))
print(rotate_array(nums, k))
