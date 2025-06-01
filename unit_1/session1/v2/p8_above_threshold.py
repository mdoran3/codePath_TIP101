def above_threshold(lst, threshold):
    new_list = []
    for i in lst:
        if i > threshold:
            new_list.append(i)
    return new_list

lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst, 10)
print(new_lst)