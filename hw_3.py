# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random

# count = int(input("Введите любое целое число: "))
# list = []
# summ = 0
# for i in range(count):
#     list.append(random.randint(0, 10))

# for i in range(1, len(list)-1, 2):
#     summ += list[i]

# print(list)
# print(summ)

# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:- [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

# import random

# count = int(input("Введите любое целое число: "))
# list1 = []
# list2 = []
# for i in range(count):
#     list1.append(random.randint(0, 10))

# if len(list1)%2 == 0:
#     l = int((len(list1)/2))
# else:
#     l = int((len(list1)/2)+1)

# for i in range(l):
#     list2.append(list1[i]*list1[-(i+1)])

# print(list1)
# print(list2)

# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# number = 10 
# # int(input("Введимте количество чисел в списке: "))
# lists = []

# for i in range(number):
#     lists.append(round(random.uniform (0, 10), 2))

# max = float(0)
# min = float(1)
# for i in lists:
#     if max < i % 1:
#         max = i % 1
#     if min > i % 1:
#         min = i % 1

# print(lists)

# print(f'{max-min:.2f}')

# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:- 45 -> 101101- 3 -> 11- 2 -> 10

# number = int(input("Введите целое число: "))
# binrevers = ""
# binnumber = ""

# while number > 0:
#     n = number % 2
#     binrevers += str(n)
#     number //=2

# print(binrevers[: : -1])    