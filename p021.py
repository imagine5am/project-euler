import math

# returns all factors except the number itself


def factors(n):
    factors = set([1])
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors


map = dict()
for i in range(1, 10000):
    map[i] = sum(factors(i))
    #print(f'{i}: {map[i]} {factors(i)}')

result = set()
for i in range(1, 10000):
    #print(f'i: {i} cond: {map[i] < 10000 and map[map[i]] == i}')
    if map[i] < 10000 and i != map[i] and map[map[i]] == i:
        print(f'result - {i}: {map[i]}')
        result.add(i)
        result.add(map[i])

print(result)

sum = 0
for i in result:
    sum += i

print(sum)

"""
Answer: 31626
"""
