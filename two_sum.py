l = int(input("Enter the length of the list: "))
nums = []
for i in range(l):
    nums.append(int(input(f"Enter the element: ")))
    
target = int(input("Enter the target sum: "))

def two_sum(nums, target):
    clectn = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                clectn.append([i, j])
    return clectn
            
print(two_sum(nums, target))

'''
Optimised solution with the help of hash table (dictionary)
'''

def opt_two_sum(nums, target):
	seen = {}
	for i, num in enumerate(nums):
		complement = target - num
		if complement in seen:
			return (seen[complement], i)
		seen[num] = i

	return ()

try:
	l = int(input("Enter the length of the list: "))
	if l < 2:
		raise ValueError("Length should be at least 2")
	nums = []
	for i in range(l):
		nums.append(int(input(f"Enter element {i+1}: ")))
	target = int(input("Enter the target sum: "))
	result = opt_two_sum(nums, target)
	if result:
		print(f"Indices of the numbers that sum to {target}: {result}")
		print(f"Numbers are: {nums[result[0]]} and {nums[result[1]]}")
	else:
		print("No solution found")

except ValueError as e:
	print(f"Invalid input: {str(e)}")