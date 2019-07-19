def isPalindrome(n):
    string = str(n)
    length = len(string)
    for i in range(0, length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True


max = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if isPalindrome(i * j) and i * j > max:
            max = i * j
print(str(max))
