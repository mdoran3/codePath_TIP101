# Flip Signs

# Plan
    # use for loop
    # return new list
    # multiply each item by -1 (to flip sign)

def flip_sign(lst):
    flipped_list = []
    if type(lst) != list:
        print("Invalid list")
    else:
        for item in lst:
            d = item * -1
            flipped_list.append(d)
    return flipped_list

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)