def factorial(n):
    """Рекурсивно вычисляет факториал числа n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("Факториал через рекурсию")
n = int(input("Введите целое число от 0 до 20: "))

if n < 0:
    print("Факториал отрицательного числа не определён")
else:
    print(f"{n}! = {factorial(n)}")
