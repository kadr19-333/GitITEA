"""Дополнительная  задача: Создать программу, которая рисует на экране прямоугольник из
звёздочек заданной пользователем  ширины и высоты."""

width = int(input("Введите ширину прямоугольника :"))
height = int(input("Введите высоту прямоугольника :"))

for h in range(height):
    for w in range(width):
        print('*', end='')
    print()