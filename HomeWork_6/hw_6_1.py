""" Задание №1.
функция что-то делает со строкой и для непечатных символов (string.whitespace)
вызывает исключение ValueError
"""
from string import whitespace


def string_processing(text, *args, **kwargs):
    try:
        result = text.upper()
        for space in text:
            if space in whitespace:
                raise ValueError()

    except ValueError as error:
        result = 'Ошибка.Incorrect value'
    return result


if __name__ == "__main__":
    text = input('Input your text: ')
    print(string_processing(text))
