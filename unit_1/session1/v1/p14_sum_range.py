def sum_positive_range(start, stop):
    sum = 0
    for i in range(start, stop+1):
        sum += i
    return sum

output = sum_positive_range(3,9)
print(output)