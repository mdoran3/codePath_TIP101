# Return doubled list

def doubled(lst):
    doubled_list = []
    if type(lst) != list:
        print("Invalid list")
    else:
        for item in lst:
            d = item * 2
            doubled_list.append(d)
    return doubled_list

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
