d = {}
def number(x):
    if len(x) != 16:
        return False
    if x[0:3] != '+7-':
        return False
    if x[6] != '-' or x[10] != '-' or x[13] != '-':
        return False
    ap = x[3:6] + x[7:10] + x[11:13] + x[14:16] 
    digits = '0123456789'
    for sym in ap:
        if not sym in digits:
            return False
    return True


def add1():
    while True:
        name = input('введите имя - ')
        if name == 'q':
            break
        phone = input('введите ваш телефон - ')
        if not number(phone):
            return False
        d[name] = phone
    return d

    
print(add1())