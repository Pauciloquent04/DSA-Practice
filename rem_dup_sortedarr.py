'''
Remove duplicates from sorted array in-place

Brute force approach
'''

def remove_duplicates(nums):
	nums = set(nums)
	nums = list(nums)
	nums.sort()
	return nums

nums = []
nums_len = int(input("Enter length of array: "))
for i in range(nums_len):
	nums.append(int(input(f"Enter element {i+1}: ")))
print(remove_duplicates(nums))

			