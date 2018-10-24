import math
# 1.
name = input('Отгадайте имя написавшего эту дичь:')
if name == 'Павел':
    print('Бинго! Вы угадали!!!)')
else:
    print('Не угадали, попробуйте ещё раз.')
#
# # 2.
x = float(input('Введите число:'))
if x >= - math.pi and x <= math.pi:
    y = math.cos(3 * x)
else:
    y = x
print('Результат функции =', y)

# 3.
random_num1 = float(input('Введите первое число:'))
random_num2 = float(input('Введите второе число:'))
if random_num1 > random_num2:
    print(random_num1 - random_num2)
elif random_num2 > random_num1:
    print(random_num2 + random_num1)
elif random_num1 == random_num2:
    print(random_num1)

# 4.
name = input("Как вас зовут?")
age = input("Сколько вам лет?")
town = input("Как называется город, в котором вы живете?")
result = "Имя:,"
print("""Имя: {},
Возраст: {}
Город: {}""".format(name, age, town))


      

