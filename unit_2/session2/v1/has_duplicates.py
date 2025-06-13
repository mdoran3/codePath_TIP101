def hasDuplicates(nums, k):
	has_duplicate = False
	duplicates = {}
	for num in range(0, k):
		if nums[num] not in duplicates:
			duplicates[num] = 1
		elif nums[num] in duplicates:
			has_duplicate = True
	return has_duplicate

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 5)
print(check2)