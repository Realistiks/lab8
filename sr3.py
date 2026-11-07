from geometry import circle_area, rectangle_area, triangle_area
from math_utils import add, multiply
from recursion_utils import factorial

print("Меню функций из модулей")
print("1 - площадь круга")
print("2 - площадь прямоугольника")
print("3 - площадь треугольника")
print("4 - сумма двух чисел")
print("5 - факториал")
print("0 - выход")

while True:
    command = input("Команда: ")

    if command == "1":
        radius = float(input("Радиус: "))
        print(f"Площадь круга: {circle_area(radius):.2f}")
    elif command == "2":
        a, b = [float(x) for x in input("Стороны: ").split()]
        print(f"Площадь прямоугольника: {rectangle_area(a, b):.2f}")
    elif command == "3":
        a, b, c = [float(x) for x in input("Стороны: ").split()]
        print(f"Площадь треугольника: {triangle_area(a, b, c):.2f}")
    elif command == "4":
        a, b = [float(x) for x in input("Два числа: ").split()]
        print(f"Сумма: {add(a, b):g}")
    elif command == "5":
        n = int(input("Число: "))
        print(f"{n}! = {factorial(n)}")
    elif command == "0":
        print("Выход")
        break
    else:
        print("Нет такой команды")
