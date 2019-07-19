number = 2 ** 1000


def digitSum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


print(digitSum(number))
