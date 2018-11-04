def hello():
    name = input('Введите  Ваше имя:')
    if not name:
        print('Hello Pavlo!')
        return
    else:
        print('Hello', name, '!')
