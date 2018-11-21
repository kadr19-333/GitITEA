""" Задание №3.
Создать функцию, которая анализирует параметры и если хотя-бы один из них
другого типа, то вызывает исключение (на выбор - одно из стандартных или своё
собственное по примеру Задания №2).
В комментарии обосновать свой выбор.

В функции main() независиимо от того было исключение или не было,
всё-равно надо сообщить с какими аргументами вы вызывали свою функцию и
какого типа был каждый аргумент.
"""


class TypeError(Exception):
    def __init__(self, string, type):
        self.string = string
        self.tp = type

def check_params_type(*args, **kwargs):
    param = {}
    for text in args:
        print(text, type(text), sep=", ")
        param.setdefault(type(text))
        if len(param) >= 2:
            raise TypeError(text, type(text))
    return param.keys()

def main():
    data = ['test1', 'test2', 'ldkfiwpopowwwc epkper', 123]

    try:
        print(check_params_type(*data))
    except TypeError as error:
        print('Ошибка:', error)


if __name__ == "__main__":
    main()
