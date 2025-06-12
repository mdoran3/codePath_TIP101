def find_divisors(n):
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)
    return divs

lst = find_divisors(30)
print(lst)