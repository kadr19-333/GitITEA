x = int(input('Введите высоту треугольника:'))
for i in range(x):
    print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()