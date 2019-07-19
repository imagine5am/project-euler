import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


count = 6
number = 13
while count != 10001:
    number += 1
    if isPrime(number):
        count += 1
print(str(number))
