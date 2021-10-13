import string
import random


def rand_ints(lenght):
    s = ''
    for i in range(lenght):
        s += random.choice(string.ascii_letters)
    return s


def count_sym(x):
    big = 0
    small = 0

    for i in x:
        if i in string.ascii_lowercase:
            small += 1
        elif i in string.ascii_uppercase:
            big += 1
    if big > small:
        return 1
    elif big < small:
        return -1
    else:
        return 0


def funct(list):
    num1 = 0
    num2 = 0
    for i in (list):
        y = count_sym(i)
        if y == 1:
            num1 += 1
        elif y == 0:
            num2 += 1
    print(rand_ints(7))
    print('Больше заглавных букв:', num1 * 100 / len(list))
    print('Больше маленьких букв:', (len(list) - num1 - num2) * 100 / len(list))
    print('Одинаково:', num2 * 100 / len(list))

print(funct([rand_ints(1), rand_ints(2), rand_ints(3), rand_ints(4), rand_ints(5), rand_ints(6), rand_ints(7)]))