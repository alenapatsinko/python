x = 0
y = 0

def init2(a, b):
    '''

    :param a: первое число
    :param b: второе число
    :return: глобальные переменные
    '''
    global x
    global y
    x = a
    y = b

def sub():
    '''

    :return: результат вычитания
    '''
    return x - y
