#g
def halve_lst(lst):
    #a
    result = []
    #b
    for number in lst:
        #d
        halved = number/2
        #c
        result.append(halved)
        
    print(result)
    #f
    return result
#e
halve_lst([2,4,6,8])
