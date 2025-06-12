def sum_even_values(dictionary):
    num_sum = 0
    
    for num in dictionary.values():
        if num % 2 == 0:
            num_sum += num
            
    return  num_sum

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))