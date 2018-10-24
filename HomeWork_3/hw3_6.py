# Если  решать по тому как написано в  задаче "Используя условные операторы if - elif осуществить проверку:"
number = float(input('Введите ЦЕЛОЕ число '))
text = 'Нет результата!'
if number >= 0 and number <= 5:
    if number == 0:
        print(0)
    elif number == 1:
        print(1)
    elif number == 2:
        print(2)
    elif number == 3:
        print(3)
    elif number == 4:
        print(4)
    elif number == 5:
        print(5)
else:
    print('Ошибка:', text)

# Но можно упростить всё:
# number = int(input('Введите число: '))
# text = 'Нет результата!'
# if number >= 0 and number <= 5:
#     print(number)
# else:
#     print('Ошибка:', text)