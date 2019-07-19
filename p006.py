square_of_sum = sum(range(101)) ** 2
sum_of_square = 0
for i in range(101):
    sum_of_square += i ** 2
print(square_of_sum - sum_of_square)
