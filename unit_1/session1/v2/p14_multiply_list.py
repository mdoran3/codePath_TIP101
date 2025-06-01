def multiply_list(lst, multiplier):
    new_lst = []
    for i in lst:
        num = i * 3
        new_lst.append(num)
    return new_lst

lst = [1,2,3]
new_lst = multiply_list(lst, 3)
print(new_lst)