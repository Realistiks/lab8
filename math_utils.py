def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b


def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b


def divide(a, b):
    """Делит a на b, при делении на ноль выбрасывает ValueError."""
    if b == 0:
        raise ValueError("деление на ноль невозможно")
    return a / b


def power(a, b):
    """Возводит a в степень b."""
    return a ** b


def average(numbers):
    """Считает среднее значение списка чисел."""
    if len(numbers) == 0:
        raise ValueError("список не должен быть пустым")
    return sum(numbers) / len(numbers)
