random_num1 = float(input('Введите первое число:'))
random_num2 = float(input('Введите второе число:'))
if random_num1 > random_num2:
    print(random_num1 - random_num2)
elif random_num2 > random_num1:
    print(random_num2 + random_num1)
elif random_num1 == random_num2:
    print(random_num1)
