def function_mul(x):
    return (3 + 2) * x


def function_div(x):
    if x == 0:  # пропускаем число 0
        return
    else:
        return (3 + 2) / x

def main_func(min, max):
    i = min
    while i <= max:
        y = function_mul(i)
        print('Функция умножения:(', i, ') = ', y, sep='')

        y = function_div(i)
        if y == None:
            print('Деление  на  0 запрещено!')
        print('Функция деления:(', i, ') = ', y, sep='')
        print('----')
        i += 0.5