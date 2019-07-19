import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    sum = 0
    i = 2
    while i < 2000000:
        if isPrime(i):
            sum += i
        i += 1
    print(sum)
