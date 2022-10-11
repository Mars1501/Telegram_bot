# # 1) Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10} 
# import math
# d = input("Введите точность: ")

# len_d = len(d) - 2
# print(f"pi = {math.pi:.{len_d}f}")

# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n = int(input('Введите натуральное число: '))

# if n > 0:
#     multipliers = []
#     while n > 1:
#         for i in range(2, n + 1):
#             count = True
#             for j in range(2, i):
#                 if i % j == 0:
#                     count = False
#                     break
#             if count:
#                 while n % i == 0:
#                     multipliers.append(i)
#                     n /= i
#     print(multipliers)
# else:
#     print('Введено не натуральное число')

# 3) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from itertools import count
# import random
# lst_1 = []
# lst_2 = []
# repeat = []
# number = int(input("Введите количество чисел в списке: "))
# for i in range(number):
#     lst_1.append(random.randint(1, 20))
# for i in range(len(lst_1)):
#     if i == len(lst_1): i -=1
#     for j in range(i + 1, len(lst_1)):
#         if lst_1[j] == lst_1[i]:
#             repeat.append(lst_1[j])
#             break
#     count = 0
#     for k in repeat:
#         if k == lst_1[i]: count += 1
#     if count == 0: lst_2.append(lst_1[i])

# print(lst_1)
# print(lst_2)
