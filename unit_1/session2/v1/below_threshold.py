def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count += 1
    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)
