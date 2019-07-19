arr = []

with open('p067_triangle.txt') as f:
    for line in f:
        arr.append(list(map(int, line.rstrip().split())))

for i in range(1, len(arr)):
    for j in range(i + 1):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif i == j:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[-1]))

"""
Answer: 7273
"""
