x = 0
y = 0

def init1(a, b):
    '''

    :param a: первое число
    :param b: второе число
    :return: глобальные переменные
    '''
    global x
    global y
    x = a
    y = b

def add():
    '''

    :return: результат сложения
    '''
    return x + y
