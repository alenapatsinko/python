"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""
# my_str = 'абвгде'
# new_str = my_str.replace('абв', '')
# print(new_str)

"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 202 конфеты. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""

Не решила
"""


"""
Создайте программу для игры в ""Крестики-нолики"".
"""
# # Задача взята из интернета. Самостоятельно сделан разбор задачи по этапам.
#
# # создается доска в диапазоне от 1 до 9 включительно
# board = list(range(1, 10))
#
# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)
#
# # предлагается ввести значение ячейки, куда поставить Х или О и проверка на корректный ввод
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       #     проверка, чтобы число было в диапазоне от 1 до 9 и в ячейке одновременно не было Х и О
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
#
# # прописываем возможные варианты выигрыша
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
#
# #прописываем очередность ходов
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         # сравниваем полученный результат с возможными вариантами выигрыша
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)
#
# input("Нажмите Enter для выхода!")выхода

"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""
# text = 'ABBCCCD'
# with open('text.txt', 'w') as ft:
#     ft.write(text)
#
# file = 'text.txt'
# with open(file, 'r') as f:
#     my_list = [i for i in f.read()]
#
# def encode(s):
#     encoding = ""  # сохраняет выходную строку
#     i = 0
#     while i < len(s):
#         # подсчитывает количество вхождений символа в индексе `i`
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         # добавляет к результату текущий символ и его количество
#         encoding += str(count) + s[i]
#         i = i + 1
#     return encoding
#
# file2 = 'text2.txt'
# with open(file2, 'w') as ft:
#     ft.write(encode(my_list))
#
#
# file2 = 'text2.txt'
# with open(file2, 'r') as fi:
#     my_list = [i for i in fi.read()]
#
# def dencode(s):
#     norm_text = ''
#     i = 0
#     while i < len(s):
#         norm_text += [f'{s[i + 1] * int(s[i])}']
#         i += 2
#     return norm_text
#
# # file2 = 'text2.txt'
# # with open(file2, 'w') as ft:
# #     ft.write(dencode(norm_text))
#
#
#

