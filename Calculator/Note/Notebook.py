# Пустотелый  треугольник
width = int(input("Первая сторона треугольника :"))
height = int(input("Вторая сторона треугольника :"))
m, n = 10, 10
for h in range(m):
    for w in range(n):
        print('*' if h in [w, m-1] or w == 0 else ' ', end='')
    print()

# b = True
# while b:
#     print("Как меня зовут?")
#     name = input('>>>')
#     if name == 'Pavlo':
#         print('bingo')
#         b = False
#
#
# my_range = range(10)
#
# iter_cas = iter(my_range)
# while True:
#     try:
#         print(next(iter_cas))




# flag = True
# while flag:
#     x = int(input('Введите первое число:'))
#     y = int(input('Введите второе число:'))
#
#     if y > x:
#         flag = False
#     else:
#         print('Введите второе число больше первого!')
#
# for i in range(x, y):
#     if i % 2 == 0:
#         print('i =', i)


# Калькульятор на мнималках!!!
# x = int(input('Введите первое число:'))
# z = input('Введи функцию + - * /:')
# y = int(input('Введите второе число:'))
#
#
# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y
# def div(x, y):
#     if y == 0:
#         return ('На ~0~ делить нельзя!')
#     else:
#         return x / y
# def mul(x, y):
#     return x * y
# while True:
#     if z == '+':
#         res = (add(x, y))
#     elif z == '-':
#         res =(sub(x, y))
#     elif z == '/':
#         res = div(x, y)
#     elif z == '*':
#         res = mul(x, y)
#     print(res)
#     break

# list = [1,2,3,4,5]
# if list[0] < list[1] and list[0] < list[2] and list[0] < list[3] and list[0] < list[4]:
#     print(list[0])
# elif list[1] < list[0] and list[1] < list[2] and list[1] < list[3] and list[1] < list[4]:
#     print(list[1])
# elif list[2] < list[0] and list[2] < list[1] and list[2] < list[3] and list[2] < list[4]:
#     print(list[2])
# elif list[3] < list[0] and list[3] < list[1] and list[3] < list[2] and list[3] < list[4]:
#     print(list[3])
# elif list[4] < list[0] and list[4] < list[1] and list[4] < list[2] and list[4] < list[3]:
#     print(list[4])

a = [1,2,3,4,5]
min_v = a[0]
for i in a:
    if i < min_v:
        min_v = i
    else:
        continue
print(min_v)