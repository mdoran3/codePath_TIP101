def count_occurrences(nums):
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    return num_count

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))