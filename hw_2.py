# 1) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# natural = int(input("Введите целое положительное число: "))
# dictionary = {}
# for i in range(1, natural + 1):
#     dictionary[i] = 3*i+1

# print(dictionary)


# 2)Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# factorial = int(input("Введите число: "))
# result = 1
# for i in range(1, factorial + 1):
#     result *=i
#     print(result, end = ", ")

# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример: Для n = 5: сумма = 11,55

# start = False
# while start == False:
#     n = int(input("Введите число: "))
#     if n >= 1:
#         start = True
#     else:
#         print("Число неверное!")
# result = 0  
# for i in range(1, n + 1):
#     result += (1 + 1 / i) ** i
# print(round(result, 2))    