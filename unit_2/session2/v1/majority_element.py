def find_majority_element(elements):
    total_elements = len(elements)
    in_majority = total_elements / 2
    num_count = {}

    for element in elements:
        if element in num_count:
            num_count[element] += 1
        else:
            num_count[element] = 1
    
    for num in num_count:
        if num_count[num] > in_majority:
            return num
        
    return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))