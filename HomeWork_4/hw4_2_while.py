# 2. С помощью while
n = int(input('Факториал числа '))
fac = 1
i = 0
if n < 0:
    print('Введите положительное число!')
else:
    while i < n:
        i += 1
        fac = fac * i
    print('Будет равен', fac)
