def isLeapYear(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    return False


def isSunday(day):
    if day == 6:
        return True
    return False


def find_day(day, month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        day += 31
    elif month in {4, 6, 9, 11}:
        day += 30
    else:
        if isLeapYear(year):
            day += 29 % 7
        else:
            day += 28 % 7
    return day % 7


if __name__ == '__main__':
    day = 1  # Since 1901 starts from Tuesday
    sunday_count = 0

    for year in range(1901, 2000 + 1):
        for month in range(1, 13):
            sunday_count += 1 if isSunday(day) else 0
            day = find_day(day, month, year)

    print(sunday_count)

    """
    Answer: 171
    """
