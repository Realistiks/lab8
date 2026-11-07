import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)


def read_int(prompt, minimum=None, maximum=None):
    """Безопасно читает целое число с проверкой границ."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            logging.warning("не целое число: %r", text)
            print("Ошибка: нужно целое число")
            continue
        if minimum is not None and value < minimum:
            logging.warning("меньше минимума: %s", value)
            print(f"Ошибка: число должно быть не меньше {minimum}")
            continue
        if maximum is not None and value > maximum:
            logging.warning("больше максимума: %s", value)
            print(f"Ошибка: число должно быть не больше {maximum}")
            continue
        return value


def read_float(prompt, minimum=None, maximum=None):
    """Безопасно читает число с плавающей точкой."""
    while True:
        text = input(prompt)
        try:
            value = float(text)
        except ValueError:
            logging.warning("не число: %r", text)
            print("Ошибка: нужно число")
            continue
        if minimum is not None and value < minimum:
            logging.warning("меньше минимума: %s", value)
            print(f"Ошибка: число должно быть не меньше {minimum}")
            continue
        if maximum is not None and value > maximum:
            logging.warning("больше максимума: %s", value)
            print(f"Ошибка: число должно быть не больше {maximum}")
            continue
        return value
