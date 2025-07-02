def find_pair_sum(s, target):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            int1 = int(s[i])
            int2 = int(s[j])
            if int1 + int2 == target:
                return True
    
    return False

s = "123456"
target = 99
print(find_pair_sum(s, target))