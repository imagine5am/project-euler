def num_to_words(n):
    string = ''
    if n > 99:
        string = unit_to_word(n // 100) + 'hundred'
        if n % 100 != 0:
            string += 'and'
    string += tens_to_word(n % 100)
    return string


def unit_to_word(n):
    return {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }[n]


def tens_to_word(n):
    map = {
        00: '',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    if map.__contains__(n):
        return map[n]
    else:
        return map[(n // 10) * 10] + unit_to_word(n % 10)


total_length = 0
for i in range(1, 1000):
    total_length += len(num_to_words(i))
total_length += len('onethousand')

print(total_length)

"""
Answer: 21124
"""
