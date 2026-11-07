from geometry import circle_area, rectangle_area, triangle_area

print("Площади фигур с обработкой ошибок")
print("1 - круг")
print("2 - прямоугольник")
print("3 - треугольник")
print("0 - выход")

while True:
    command = input("Команда: ")
    try:
        if command == "1":
            radius = float(input("Радиус: "))
            print(f"Площадь круга: {circle_area(radius):.2f}")
        elif command == "2":
            a, b = [float(x) for x in input("Стороны: ").split()]
            print(f"Площадь прямоугольника: {rectangle_area(a, b):.2f}")
        elif command == "3":
            a, b, c = [float(x) for x in input("Стороны: ").split()]
            print(f"Площадь треугольника: {triangle_area(a, b, c):.2f}")
        elif command == "0":
            print("Выход")
            break
        else:
            print("Нет такой команды")
    except ValueError as error:
        print("Ошибка:", error)
