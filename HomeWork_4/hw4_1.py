# Даны числа  а и b (a < b). Вывести сумму всх натуральных чисел от  а до b (включительно).
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
if a and b >= 0 and a < b:
    sum = (b + a) * (b - a + 1)/2
    print('Суммка натуральных чисел этого диапазона = ', sum)
else:
    print('Ошибка! Число должно  быть натуральным!')


