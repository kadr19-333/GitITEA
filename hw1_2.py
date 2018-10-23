# 1.
a = float(input('Введите сторону "а":'))
b = float(input('Введите сторону "b":'))
c = float(input('Введите сторону "c":'))

p = 0.5 * (a + b + c)
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if p == a or p == b or p == c:
    print('Стороны треугольника введены неправильно!')
else:
    print('Площадь треугольника по формуле  Герона  =', s)

# 2.
a1 = 4
b1 = 6
let = 2
print(a1, b1)
a1 = 4 + let
b1 = 6 - let
print(a1, b1)

# 3.
x = 5
y = 10
print(x, y)

x = x + y
y = x - y
x = x - y
print(x, y)

# 4.
some_numder = int(input('Введите число >>>'))
if some_numder % 2 == 0:
    print(some_numder ** 2)
else:
    print(some_numder * 2)