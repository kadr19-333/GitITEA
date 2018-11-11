
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


MATH_OPERATION = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul
}


def user_input():
    vvod = True
    while vvod:
        try:
            num1 = float(input('Введите первое число: '))
            while True:
                operation = input('Выберите функцию:| + | - | / | * |: ')
                if operation in MATH_OPERATION:
                    break
                else:
                    print('Введите знак из списка: + or - or / or * ')
            while True:
                num2 = float(input('Введите второе число: '))
                if operation == '/' and num2 == 0:
                    print('Ошибка! Деление на  ноль запрещено!')
                else:
                    break

            return {
                'num1': num1,
                'operation': operation,
                'num2': num2
            }
        except ValueError as error:
            print('Ошибка', error)
            print('Попробуейте ещё раз')
            print()


def main():
    input_from_user = user_input()
    res = MATH_OPERATION[input_from_user['operation']](input_from_user['num1'], input_from_user['num2'])
    if res:
        print('Результат:', input_from_user['num1'], input_from_user['operation'], input_from_user['num2'],'=', res)

main()

# 1) Уточнить как  добавить цикл на  безконечные вычисления, пока не введешь стоп слово.
# 2) Уточнить по какой причине  в консоле  отображается  ошибка. А так же пути решения проблемы.
# if res.is_integer == True:
#     print(int(res))
# else:
#     print(res)
#
# if res % 2 == 0:
#     print(int(res))
# else:
#     print(res)