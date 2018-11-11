# first_katet = int(input('Введи 1й катет треугольника:'))
# second_katet = int(input('Введи 2й катет треугольника:'))
#
#
# def gipo(a, b):
#     def summa():
#         return a ** 2 + b ** 2
#
#     return summa() ** 0.5
#
#
# result = gipo(first_katet, second_katet)
# print('Гипотенуза равна:', result)
#
#
# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print('на 0 делить не нуна!')

def func():
    xaxa = True

    while xaxa:
        try:
            num1 = int(input('Первое число >>>'))
            operation = input('Знак поделить >>>')
            num2 = int(input('Второе число >>>'))
            print('Result:', num1 / num2)
            xaxa = False

        except (ValueError, ZeroDivisionError) as error:
            print('Ошибка', error)
            print('Попробуейте ещё раз')
            print()

func()

def add(a, b):
    return a + b
def sub(a, b):
    return a - b


