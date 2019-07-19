def fact(n):
    prod = n
    for i in range(n - 1, 1, -1):
        prod *= i
    return prod


def update_target_rank(rank, fact_val, objects, output, i):
    rank += fact_val * i
    output.append(objects[i])
    del objects[i]
    return rank


if __name__ == '__main__':
    target_rank = 1000000  # given
    objects = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rank = 0
    i = len(objects) - 1
    output = []
    while rank != target_rank - 1:
        fact_val = fact(i)
        for j in range(i + 1):
            if rank + fact_val * j > target_rank - 1:
                rank = update_target_rank(rank, fact_val, objects, output, j - 1)
                break
            elif j == i and rank + fact_val <= target_rank + 1:
                rank = update_target_rank(rank, fact_val, objects, output, i)
                break
        i -= 1
    output.extend(objects)
    print(output)
