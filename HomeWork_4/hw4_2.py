import math
# Создать программу, которая вычисляет факториал введённого пользователем числа.
# 1.С помощью модуля math
number = int(input('Число: >>>'))
print('Факториал введённого числа =', math.factorial(number))

# 2. С помощью while
n = int(input('Факториал числа '))
fac = 1
i = 0
while i < n:
     i += 1
     fac = fac * i
print('Будет равен', fac)

