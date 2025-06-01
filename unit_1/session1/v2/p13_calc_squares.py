def squares(nums):
    new_lst = []
    for i in nums:
        square_num = i ** 2
        new_lst.append(square_num)
    return new_lst

print(squares([1,2,3,4]))