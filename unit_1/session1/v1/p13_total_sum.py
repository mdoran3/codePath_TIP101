def sum_positive_range(stop):
    sum = 0
    for i in range(1, stop+1):
        sum += i
    return sum

output = sum_positive_range(6)
print(output)