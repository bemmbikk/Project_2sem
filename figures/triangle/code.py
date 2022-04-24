__all__ = ['triangle_perimeter', 'triangle_area']
from math import sqrt as s


def triangle_perimeter(a=7, b=2, c=8):
    return print('периметр треугольника: ', a + b + c)


def triangle_area(a=7, b=2, c=8):
    p = (a + b + c) / 2
    return print('площадь треугольника: ', s(p + (p - a) * (p - b) * (p - c)))
