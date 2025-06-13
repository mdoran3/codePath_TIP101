def divideList(nums):
    if len(nums) % 2 != 0:
        return False
    
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) +1
   
    for val in count.values():
        if val % 2 != 0:
            return False
    return True

nums = [3,2,3,2,2,2]
print(divideList(nums))

nums = [1,2,3,4]
print(divideList(nums))