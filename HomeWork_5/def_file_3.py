def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


def check_operation(x, operation, y):
    res = None
    if operation == '+':
        res = add(x, y)
    elif operation == '-':
        res = sub(x, y)
    elif operation == '*':
        res = mul(x, y)
    elif operation == '/':
        res = div(x, y)
    else:
        res = 'Error'
        print(res)

    return res


def main(first, operation, second):
    result_of_function = check_operation(first, operation, second)
    if result_of_function != "Error":
        print('Результат равен: ', result_of_function)
