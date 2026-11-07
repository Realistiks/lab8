import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    """Число Фибоначчи с кэшированием результатов."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_plain(n):
    """Число Фибоначчи без кэширования."""
    if n < 2:
        return n
    return fib_plain(n - 1) + fib_plain(n - 2)


print("Число Фибоначчи")
n = int(input("Введите n: "))

start = time.perf_counter()
value = fib(n)
time_cached = time.perf_counter() - start

print()
print(f"F({n}) = {value}")
print(f"С кэшированием: {time_cached * 1000:.3f} мс")

if n <= 32:
    start = time.perf_counter()
    plain = fib_plain(n)
    time_plain = time.perf_counter() - start
    print(f"Без кэширования: {time_plain * 1000:.3f} мс")
    print("Результаты совпадают:", value == plain)
    if time_cached > 0:
        print(f"Ускорение: {time_plain / time_cached:.0f} раз")
