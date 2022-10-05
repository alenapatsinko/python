"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

# my_list = [2, 3, 5, 9, 3]
# i = 0
# s = 0
# for i in range(0, len(my_list)-1, 2):
#     i = i + 1
#     print(my_list[i])
#     s = s + my_list[i]
# print(s)

# # новое решение
# my_list = [2, 3, 5, 9, 3]
# for i in range(1, len(my_list)-1, 2):
#     f = lambda x, y: x+y
# print(f(my_list[i], my_list[i+1]))


"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

# num = int(input('введите число '))
# a = []
# for i in range(1, num+1):
#     if num % i == 0:
#         a.append(i)
# print(a)

# Новое решение
# num = int(input('введите число '))
# n = [i for i in range(1, num+1) if num % i == 0]
# print(n)

"""
Есть N натуральных чисел, записанных через пробел. 
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 == A[i-1]. Найдите это число.
my_str = ‘1 2 3 5 6’ => 4
"""
# my_str = '1 2 3 4 6'
# my_str = list(map(int, my_str.split()))
# ms = [i for i in range(1, len(my_str)) if my_str[i] - my_str[i-1] > 1]
# print(sum(ms,1))

"""
 Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл users_hobby.txt.
Фрагмент файла с данными о пользователях (users.txt):
Иванов Иван Иванович
Петров Петр Петрович
Фрагмент файла с данными о хобби (hobby.txt):
скалолазание, охота
горные лыжи
"""

# user_hobby = {}
#
# with open('users.txt', encoding='utf-8') as users:
#     with open('hobby.txt', encoding='utf-8') as hobby:
#         for line_user, line_user_hobby in zip(users, hobby):
#             # user_hobby[line_user.replace('\n', '')] = line_user_hobby.replace('\n', '')
#             user_hobby[line_user.replace('\n', '')] = line_user_hobby
#
# print(user_hobby)
#
# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     for key, val in user_hobby.items():
#         f.writelines(f'{key}: {val}')


# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     with open('users.txt', encoding='utf-8') as users:
#         with open('hobby.txt', encoding='utf-8') as hobby:
#             for line_user, line_user_hobby in zip(users, hobby):
#                 f.writelines(f'{line_user.strip()}: {line_user_hobby}')
