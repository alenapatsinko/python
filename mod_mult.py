x = 0
y = 0

def init3(a, b):
    '''

    :param a: первое чилсло
    :param b: второе число
    :return: глобальные переменные
    '''
    global x
    global y
    x = a
    y = b

def mult():
    '''

    :return: результат умножения
    '''
    return x * y
