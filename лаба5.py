from input_utils import read_int, read_float

print("Безопасный ввод данных")
print("Ошибки записываются в errors.log")
print()

age = read_int("Возраст: ", 1, 120)
score = read_float("Средний балл: ", 0, 5)

print()
print(f"Возраст: {age}")
print(f"Средний балл: {score:.2f}")
