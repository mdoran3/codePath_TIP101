def reverse_list(nums):
    # Your code here
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        tmp = nums[p1]
        nums[p1] = nums[p2]
        nums[p2] = tmp
        p1 += 1
        p2 -= 1
    return nums

# Example:
print(reverse_list([1, 2, 3, 4, 5]))  # Expected output: [5, 4, 3, 2, 1]