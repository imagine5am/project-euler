import collections


def prime_factorise(n):
    x = []
    for i in range(2, n // 2 + 1):
        while n % i == 0:
            x.append(i)
            n = n // i
    if not len(x):
        x.append(n)
    return x


if __name__ == '__main__':
    initial_product = 2520
    initial_factors_map = collections.Counter(prime_factorise(initial_product))

    for i in range(20, 10, -1):
        temp_factorization = prime_factorise(i)
        temp_factors_map = collections.Counter(temp_factorization)
        for key in temp_factors_map:
            if initial_factors_map[key] <= temp_factors_map[key]:
                initial_product *= key ** (temp_factors_map[key] - initial_factors_map[key])
                initial_factors_map[key] += (temp_factors_map[key] - initial_factors_map[key])

    print(str(initial_product))
    # print('-----------------**********************-----------------')
    # print(factors(product))
