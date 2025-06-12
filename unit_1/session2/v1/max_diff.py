# Max Different

# Plan
    # Sort list
    # Defined max and min by first and last index
    # Subtract min from max to get diff
    # return diff

def max_difference(lst):
    if type(lst) != list:
        print("Invalid list")
    else:
        lst.sort()
        last = len(lst)
        max = lst[last - 1]
        min = lst[0]
        diff = max - min  
        print(lst)
    return diff

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
