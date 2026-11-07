def is_prime(n):
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


print("Проверка числа на простоту")
n = int(input("Введите число: "))

if is_prime(n):
    print(f"{n} — простое число")
else:
    print(f"{n} — не простое число")
