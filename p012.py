import math


def factors(n):
    x = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            x.add(i)
            x.add(n // i)
    return x


i = 1
triangle_num = 0
while True:
    i += 1
    triangle_num = int((i ** 2 / 2) + (i / 2))
    if len(factors(triangle_num)) > 500:
        break
print(str(triangle_num))

"""
Answer: 76576500
"""
