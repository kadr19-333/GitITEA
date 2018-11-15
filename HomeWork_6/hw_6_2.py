from string import whitespace


class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol


def string_processing(text, *args, **kwargs):
    result = text.upper()
    n = 0
    for space in text:
        n += 1
        if space in whitespace:
            raise WhitespaceError(n, space)
    print(result)
    return result


def main():
    try:
        string_processing(text='Проверка программы!')
    except WhitespaceError as error:
        print('Ошибка в символе № {}. Проблемный симмвол {}!'.format(error.position, repr(error.symbol)))


if __name__ == "__main__":
    main()
