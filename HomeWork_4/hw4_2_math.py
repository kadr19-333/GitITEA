import math
# Создать программу, которая вычисляет факториал введённого пользователем числа.

number = int(input('Число: >>>'))
if number < 0:
    print('Введите положительное число!')
else:
    print('Факториал введённого числа =', math.factorial(number))