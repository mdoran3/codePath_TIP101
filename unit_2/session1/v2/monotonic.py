def is_monotonic(nums):
    is_decreasing = True
    is_increasing = True
    for num in range(len(nums) - 1):
        if nums[num] <= nums[num+1]:
            continue
        else:
            is_increasing = False
    for num in range(len(nums) - 1):
        if nums[num] >= nums[num+1]:
            continue
        else:
            is_decreasing = False
    if is_increasing is True or is_decreasing is True:
        return True
    else:
        return False
         
    
nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))
nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))
nums3 = [1,1,1]
print(is_monotonic(nums3))
nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))