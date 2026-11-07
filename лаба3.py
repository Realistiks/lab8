from math_utils import add, subtract, multiply, divide, power, average

print("Калькулятор на модуле math_utils")
print("Введите два числа")
a = float(input())
b = float(input())

print()
print(f"Сумма: {add(a, b):g}")
print(f"Разность: {subtract(a, b):g}")
print(f"Произведение: {multiply(a, b):g}")

try:
    print(f"Частное: {divide(a, b):g}")
except ValueError as error:
    print("Частное: ошибка —", error)

print(f"Степень: {power(a, b):g}")
print(f"Среднее: {average([a, b]):g}")
