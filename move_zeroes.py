'''
Moving zeroes at the end of the array

brute force approach
'''

def move_zeroes(nums):
	slow = None
	for i in range(len(nums)):
		if (nums[i] == 0) and (slow is None):
			slow = i
		elif (slow is not None) and (nums[i] != 0):
			nums[i], nums[slow] = nums[slow], nums[i]
			slow += 1
	return nums
'''
nums = []
len_nums = int(input("Enter the length of array: "))
for i in range(len_nums):
	nums.append(int(input(f"Enter element {i+1}: ")))
print(move_zeroes(nums))
'''
'''
More refined solution
'''

def refined_move_zeroes(nums):
    non_zero_pos = 0  # Tracks the position for the next non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero_pos] = nums[non_zero_pos], nums[i]
            non_zero_pos += 1
    return nums

nums = []
len_nums = int(input("Enter the length of array: "))
for i in range(len_nums):
    nums.append(int(input(f"Enter element {i+1}: ")))

print(move_zeroes(nums))
print(refined_move_zeroes(nums))