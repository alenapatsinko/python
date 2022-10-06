x = 0
y = 0

def init4(a, b):
    '''

    :param a: первое число
    :param b: второе число
    :return: глобальные переменные
    '''
    global x
    global y
    x = a
    y = b

def div():
    '''

    :return: результат деления нацело
    '''
    return x // y
