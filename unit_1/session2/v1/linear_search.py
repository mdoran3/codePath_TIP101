def linear_search(lst, target):
    index = -1
    for i in range(len(lst)):
        if lst[i] == target:
            index = i
    return index
            
lst = [1,4,5,2,8]
position = linear_search(lst,8)
print(position)