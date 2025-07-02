def merge_sorted_lists(nums1, nums2):
    # Your code here
    p1 = 0
    p2 = 0
    merged = []

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            merged.append(nums1[p1])
            p1 += 1
        else:
            merged.append(nums2[p2])
            p2 += 1
        
    while p1 < len(nums1):
        merged.append(nums1[p1])
        p1 += 1

    while p2 < len(nums2):
        merged.append(nums2[p2])
        p2 += 1
    return merged

# Example:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Expected: [1, 2, 3, 4, 5, 6]