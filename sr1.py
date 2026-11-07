from geometry import circle_area, rectangle_area, triangle_area

print("Площади фигур")
radius = float(input("Радиус круга: "))
a, b = [float(x) for x in input("Стороны прямоугольника: ").split()]
x, y, z = [float(x) for x in input("Стороны треугольника: ").split()]

print()
print(f"Круг: {circle_area(radius):.2f}")
print(f"Круг с точностью 4 знака: {circle_area(radius, 4):.4f}")
print(f"Прямоугольник: {rectangle_area(a, b):.2f}")
print(f"Треугольник: {triangle_area(x, y, z):.2f}")
