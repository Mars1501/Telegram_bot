# 1) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    # a) Добавьте игру против бота
    # b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите сколько конфет возьмете (число от 1 до 28): "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, такое количество конфет брать нельзя! \
#             \n Введите количество конфет (число от 1 до 28): "))
#     return x


# def res_out_print(name, k, count, value):
#     print(f"Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.")

# name1, name2 = "Человек", "БотA"
# value = 100
# flag = randint(0,2)  # очередность: 0 - человек, 1 - БотА
# if flag:
#     print(f"Первый ходит {name1}")
# else:
#     print(f"Первый ходит {name2}")

# k = int(121 % 28)
# count1 = 0 
# count2 = 0
# if flag:                   # Первый ход - случайное число 
#         print(f'{name1}, если хочешь победить, бери {k} штук в первый раз, а потом смотри подсказки на экране')
#         count1 += k
#         value -= k
#         flag = False
#         res_out_print(name1, k, count1, value)
# else:
#     flag = False
#     res_out_print(name2, k, count2, value)

# while value > 28:
#     if flag:
#         k = input_dat(name1)
#         count1 += k
#         value -= k
#         flag = False
#         res_out_print(name1, k, count1, value)
#     else:
#         k = randint(1,29)
#         count2 += k
#         value -= k
#         flag = True
#         res_out_print(name2, k, count2, value)

# if flag:
#     print(f"Выиграл {name1}")
# else:
#     print(f"Выиграл {name2}")


# Вариант человек против БотаВ с интеллектом, знающего стратегию. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# from random import randint


# def input_dat(name):
#     x = int(input(f"{name}, введите сколько конфет возьмете (число от 1 до 28): "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, такое количество конфет брать нельзя! \
#             \n Введите количество конфет (число от 1 до 28): "))
#     return x

# def res_out_print(name, k, count, value):
#     print(f"Ход: {name}, взял {k}, теперь у него {count}. В кучке сталось {value} конфет.")

# name1, name2 = "Человек", "БотВ"
# value = 121
# flag = randint(0,2)            
# if flag:
#     print(f"Первый ходит {name1}")
# else:
#     print(f"Первый ходит {name2}")
    
# k = int(121 % 28)
# count1 = k
# value = value - k
# if flag:                   
#         flag = False
#         res_out_print(name1, k, count1, value)
# else:
#     flag = False
#     res_out_print(name2, k, count2, value)
# while value > 28:
#     if flag:
#         k = input_dat(name1)
#         count1 += k
#         value -= k
#         flag = False
#         res_out_print(name1, k, count1, value)
#     else:
#         k = input_dat(name2)
#         count2 += k
#         value -= k
#         flag = True
#         res_out_print(name2, k, count2, value)

# if flag:
#     print(f"Выиграл {name1}")
# else:
#     print(f"Выиграл {name2}")

# 2) Создайте программу для игры в ""Крестики-нолики"".
# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = [i for i in range(1,10)]

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", '\033[36m{}'.format(board[0+i*3]), \
#             '\033[0m{}'.format("|"), '\033[36m{}'.format(board[1+i*3]), \
#             '\033[0m{}'.format("|"), '\033[36m{}'.format(board[2+i*3]), \
#             '\033[0m{}'.format("|"))
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = '\033[0m{}'.format(player_token)
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_victory(board):
#    victory_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in victory_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

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
#         if counter > 4:
#            tmp = check_victory(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")


# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. 
# 
def coding(cod_in):
    count = 1
    cod_out = ''
    for i in range(len(cod_in) - 1):
        if cod_in[i] == cod_in[i + 1]:
            count += 1
        else:
            cod_out += str(count) + ' ' + cod_in[i] + ' '
            count = 1
    if count > 1 or (cod_in[-2] != cod_in[-1]):
        cod_out += str(count) + ' ' + cod_in[-1]
    return cod_out

def decoding(cod_in):
    list_cod_in = cod_in.split()
    print(list_cod_in)
    decod_out = ''
    i = 0
    while i < len(list_cod_in):
        decod_out += str(list_cod_in[i + 1])*(int(list_cod_in[i]))
        i += 2
    return decod_out
  
string_new = input('Введите данные для сжатия: ')
with open('file_1.txt', 'w') as f1:
    f1.write(string_new)

with open('file_1.txt', 'r') as f1:
    str1 = f1.read()
print(str1)

rar_str = coding(str1)
print(f'Результат сжатия: {rar_str}')

with open('file_1.txt', 'w') as f2:
    f2.write(rar_str)
    
rar_str1 = decoding(rar_str)
print(f'Результат восстановления: {rar_str1}')

with open('file_1.txt', 'w') as f2:
    f2.write(rar_str1)
