def factorial(n):
    """Рекурсивно вычисляет факториал числа n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def digit_sum(n):
    """Рекурсивно считает сумму цифр числа."""
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def reverse(text):
    """Рекурсивно переворачивает строку."""
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


def is_palindrome(text):
    """Рекурсивно проверяет, является ли строка палиндромом."""
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def binary_search(arr, key, left, right):
    """Рекурсивный бинарный поиск в отсортированном списке."""
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == key:
        return mid
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, right)
    return binary_search(arr, key, left, mid - 1)
