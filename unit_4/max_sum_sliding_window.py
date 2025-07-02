def max_sum_of_three(nums):
    # Your code here
    p1 = 0
    p2 = 2
    max_sum = 0
    max = 0

    while p2 <= len(nums):
        max = sum(nums[p1:p2+1])
    
        if max > max_sum:
            max_sum = max
        
        p1 += 1
        p2 += 1

    return max_sum

# Example:
print(max_sum_of_three([1, 4, 2, 10, 23, 3, 1, 0, 20]))  # Expected: 36 (10 + 23 + 3)