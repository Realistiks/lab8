from recursion_utils import digit_sum, reverse, is_palindrome, binary_search

print("Рекурсивные алгоритмы")
print("1 - сумма цифр числа")
print("2 - переворот строки")
print("3 - проверка палиндрома")
print("4 - бинарный поиск")
print("0 - выход")

while True:
    command = input("Команда: ")

    if command == "1":
        n = int(input("Число: "))
        print("Сумма цифр:", digit_sum(abs(n)))
    elif command == "2":
        text = input("Строка: ")
        print("Перевёрнутая строка:", reverse(text))
    elif command == "3":
        text = input("Строка: ").lower()
        if is_palindrome(text):
            print("Это палиндром")
        else:
            print("Это не палиндром")
    elif command == "4":
        print("Отсортированные числа через пробел")
        arr = [int(x) for x in input().split()]
        key = int(input("Что искать: "))
        index = binary_search(arr, key, 0, len(arr) - 1)
        if index == -1:
            print(f"Числа {key} нет в списке")
        else:
            print(f"Число {key} найдено на позиции {index}")
    elif command == "0":
        print("Выход")
        break
    else:
        print("Нет такой команды")
