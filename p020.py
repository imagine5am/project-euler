def factorial(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod


def digitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum


print(digitSum(factorial(100)))

"""
Answer: 648
"""
