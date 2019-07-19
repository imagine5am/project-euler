import math


def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return divisors


def isAbundant(n):
    if sum(proper_divisors(n)) > n:
        return True
    return False


"""
# modified binary search
def search_min_successor(nums, n):
    last = len(n) - 1
    start = 0
    mid = start + last // 2
    while num[mid] != n:

    return mid
"""


def search_min_successor(arr, element):
    for i in range(len(arr)):
        if arr[i] >= element:
            return i - 1


if __name__ == '__main__':
    abundant_nums = [12]
    for i in range(13, 28123):
        if isAbundant(i):
            abundant_nums.append(i)

    total = sum(range(23))

    # print(abundant_nums)

    for i in range(25, 28124):
        # check if 'i' can be written as a sum of two abundant numbers
        start = 0
        end = search_min_successor(abundant_nums, i)
        flag = True
        # print(i)
        while start < end:
            if i == abundant_nums[start] + abundant_nums[end]:
                flag = False
                break
            elif i > abundant_nums[start] + abundant_nums[end]:
                start += 1
            elif i < abundant_nums[start] + abundant_nums[end]:
                end -= 1
        if flag:
            total += i

    print(total)
