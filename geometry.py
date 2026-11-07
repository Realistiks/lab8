import math


def circle_area(radius, digits=2):
    """Площадь круга с заданной точностью."""
    if radius < 0:
        raise ValueError("радиус не может быть отрицательным")
    return round(math.pi * radius ** 2, digits)


def rectangle_area(a, b):
    """Площадь прямоугольника."""
    if a <= 0 or b <= 0:
        raise ValueError("стороны должны быть положительными")
    return a * b


def triangle_area(a, b, c):
    """Площадь треугольника по формуле Герона."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("стороны должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("такого треугольника не существует")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
