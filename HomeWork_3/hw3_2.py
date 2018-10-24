import math

x = float(input('Введите число:'))
if x >= - math.pi and x <= math.pi:
    y = math.cos(3 * x)
else:
    y = x
print('Результат функции =', y)
