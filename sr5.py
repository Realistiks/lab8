print("Введите слова через пробел")
words = input().split()

ordered = sorted(words, key=lambda word: (len(word), word))

print()
print("Сортировка по длине, затем по алфавиту:")
for word in ordered:
    print(f"{len(word):>2}  {word}")
