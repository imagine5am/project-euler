def seqCount(n):
    count = 1
    term = n
    while term != 1:
        if term % 2 == 0:
            term = term // 2
        else:
            term = 3 * term + 1
        count += 1
    return count


max_length = 0
number = 0
for i in range(1, 1000000):
    temp = seqCount(i)
    if temp > max_length:
        max_length = temp
        number = i
print(number)
