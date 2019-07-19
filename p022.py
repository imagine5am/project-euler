def alphabeticValue(n):
    return{
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }[n]


def name_score(name):
    score = 0
    for i in range(len(name)):
        score += alphabeticValue(name[i])
    return score


if __name__ == '__main__':
    names = []
    with open('p022_names.txt') as f:
        for line in f:
            names.extend(line.lower().replace('"', '').split(','))
    names.sort()

    sum = 0
    for i in range(len(names)):
        sum += (i + 1) * name_score(names[i])

    print(sum)


"""
Answer: 871198282
"""
