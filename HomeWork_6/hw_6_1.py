""" Задание №1.
функция что-то делает со строкой и для непечатных символов (string.whitespace)
вызывает исключение ValueError
"""
from string import whitespace


def string_processing(text, *args, **kwargs):
    result = text.upper()
    for space in text:
        if space in whitespace:
            raise ValueError('Вы ввели неподходящий символ!')
    print(result)
    return result


if __name__ == "__main__":
    try:
        string_processing(text = 'kdjfj ldjkffkf')
    except ValueError as error:
        print('Ошибка!!! - ', error)





