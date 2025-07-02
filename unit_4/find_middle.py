def find_middle(lst):
    slow = fast = 0
    while fast < len(lst) and fast+1 < len(lst):
        slow += 1
        fast += 2
    return lst[slow]

print(find_middle([1,2,3,4,5,6]))