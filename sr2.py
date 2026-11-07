import time


def power_recursive(base, exp):
    """Быстрое возведение в степень через рекурсию."""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power_recursive(base, exp // 2)
        return half * half
    return base * power_recursive(base, exp - 1)


def power_iterative(base, exp):
    """Возведение в степень циклом."""
    result = 1
    for _ in range(exp):
        result *= base
    return result


print("Введите основание и степень через пробел")
base, exp = [int(x) for x in input().split()]

repeats = 1000

start = time.perf_counter()
for _ in range(repeats):
    value_rec = power_recursive(base, exp)
time_rec = time.perf_counter() - start

start = time.perf_counter()
for _ in range(repeats):
    value_it = power_iterative(base, exp)
time_it = time.perf_counter() - start

start = time.perf_counter()
for _ in range(repeats):
    value_builtin = base ** exp
time_builtin = time.perf_counter() - start

print()
if exp <= 20:
    print(f"Результат: {value_rec}")
else:
    print(f"Результат: число из {len(str(value_rec))} цифр")
print(f"{'Способ':<10}{'Время, мс':>12}")
print("-" * 22)
print(f"{'Рекурсия':<10}{time_rec * 1000:>12.2f}")
print(f"{'Цикл':<10}{time_it * 1000:>12.2f}")
print(f"{'**':<10}{time_builtin * 1000:>12.4f}")
print("Все результаты совпадают:", value_rec == value_it == value_builtin)
