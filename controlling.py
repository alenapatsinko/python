from view import get_choise_sign, get_choise_num, get_result
from mod_add import add, init1
from mod_sub import sub, init2
from mod_mult import mult, init3
from mod_div import div, init4
from rational import get_rational
from coplex import get_complex
from log import get_logger

def button_click():
    numb = get_choise_num()
    if numb == 1:
        a =get_rational()
        b = get_rational()
        sign = get_choise_sign()
        if sign == '+':
            init1(a, b)
            result = add()
        elif sign == '-':
            init2(a, b)
            result = sub()
        elif sign == '*':
            init3(a, b)
            result = mult()
        elif sign == '/':
            init4(a, b)
            result = div()
        get_logger(sign, result)
        get_result(result)
    else:
        a = get_complex()
        b = get_complex()
        sign = get_choise_sign()
        if sign == '+':
            init1(a, b)
            result = add()
        elif sign == '-':
            init2(a, b)
            result = sub()
        elif sign == '*':
            init3(a, b)
            result = mult()
        elif sign == '/':
            init4(a, b)
            result = ('действие нельзя выполнить')
        get_logger(sign, result)
        get_result(result)