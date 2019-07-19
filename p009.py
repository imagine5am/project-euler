for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                print(f'{i} * {j} * {k} = {i * j * k}')
